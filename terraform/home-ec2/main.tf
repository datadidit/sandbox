# Automatically query your current local workstation's public IP
data "http" "my_public_ip" {
  url = "https://ifconfig.me/ip"
}

# Creates the security group needed for connecting only from your local box
resource "aws_security_group" "ssh_restricted" {
  name        = "ssh-only-my-ip"
  description = "Block all inbound SSH access except for the deployer workspace"

  ingress {
    description = "SSH from my workstation only"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    # Append the /32 routing suffix dynamically to lock it to your single IP
    cidr_blocks = ["${chomp(data.http.my_public_ip.response_body)}/32"]
  }

  egress {
    description = "Allow all outbound infrastructure traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
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
    ami = data.aws_ami.ami.id
    instance_type = var.aws_instance_type
    vpc_security_group_ids = concat([aws_security_group.ssh_restricted.id], var.aws_additional_security_groups)
    key_name  = data.aws_key_pair.key_pair.key_name
    user_data = var.aws_instance_startup_script
}