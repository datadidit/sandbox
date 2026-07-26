# Pulls the AWS Subnet if provided by the user.
data "aws_subnet" "subnet" {
  count = var.aws_subnet_id != null ? 1 : 0
  id    = var.aws_subnet_id
}

locals {
  current_timestamp   = timestamp()
  formatted_timestamp = formatdate("YYYY-MM-DD'T'hh:mmZ", local.current_timestamp)
}

locals {
  # Just pull out the first default subnet
  provided_subnet = var.aws_subnet_id != null ? data.aws_subnet.subnet[0].id : null
}

data "external" "local_user" {
  program = ["sh", "-c", "echo \"{\\\"user\\\": \\\"$(whoami)\\\"}\""]
}

data "external" "force_ipv4" {
  program = ["sh", "-c", "echo \"{\\\"ipv4\\\": \\\"$(curl -4 ifconfig.me)\\\"}\""]
}

# Automatically query your current local workstation's public IP
data "http" "my_public_ip" {
  url = "https://ifconfig.me/ip"
}

locals {
  is_ipv6 = can(regex(":", data.http.my_public_ip.response_body))
}

# 1. Base Security Group Container (Always created)
resource "aws_security_group" "ssh_restricted" {
  name        = "ssh-only-my-ip-test"
  description = "Block all inbound SSH access except for the deployer workspace"
}

# ==========================================
# IPv4 Rules (Created when local.is_ipv6 = false)
# ==========================================

# Ingress: SSH via IPv4
# TODO: figure out how to make this work.
resource "aws_vpc_security_group_ingress_rule" "ssh_ingress_v4" {
  # TODO: If you can figure out the ipv6 rule hanging then you can make this conditional
  # count             = !local.is_ipv6 ? 1 : 0
  security_group_id = aws_security_group.ssh_restricted.id
  description       = "SSH from my workstation (IPv4)"

  ip_protocol = "tcp"
  from_port   = 22
  to_port     = 22
  cidr_ipv4   = "${chomp(data.external.force_ipv4.result["ipv4"])}/32"
}

# Ingress: SSH via IPv6
# TODO: Below does not work need to figure out proper way to set this up...
resource "aws_vpc_security_group_ingress_rule" "ssh_ingress_v6" {
  count             = local.is_ipv6 ? 1 : 0
  security_group_id = aws_security_group.ssh_restricted.id
  description       = "SSH from my workstation (IPv6)"

  ip_protocol = "tcp"
  from_port   = 22
  to_port     = 22
  cidr_ipv6   = "${chomp(data.http.my_public_ip.response_body)}/128"
}

# Egress: All Outbound via IPv4
resource "aws_vpc_security_group_egress_rule" "all_egress_v4" {
  security_group_id = aws_security_group.ssh_restricted.id
  description       = "Allow all outbound IPv4 traffic"

  ip_protocol = "-1"
  cidr_ipv4   = "0.0.0.0/0"
}

# ==========================================
# IPv6 Rules (Created when local.is_ipv6 = true)
# ==========================================

# Egress: All Outbound via IPv6
resource "aws_vpc_security_group_egress_rule" "all_egress_v6" {
  security_group_id = aws_security_group.ssh_restricted.id
  description       = "Allow all outbound IPv6 traffic"

  ip_protocol = "-1"
  cidr_ipv6   = "::/0"
}

# Key pair ssh
data "aws_key_pair" "key_pair" {
  key_name = var.aws_key_pair_name
}

# Try filtering things out
data "aws_ami" "ami" {
  most_recent = true
  owners      = ["amazon"] # Official Canonical AWS Account ID

  filter {
    name   = "image-id"
    values = [var.aws_ami_image_id]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "ec2_instance" {
  ami                    = data.aws_ami.ami.id
  instance_type          = var.aws_instance_type
  vpc_security_group_ids = concat([aws_security_group.ssh_restricted.id], var.aws_additional_security_groups)
  key_name               = data.aws_key_pair.key_pair.key_name
  user_data              = var.aws_instance_startup_script
  subnet_id              = local.provided_subnet
  tags = {
    Name = var.aws_ec2_instance_name
  }
}