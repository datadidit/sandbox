# Create the Webserver EC2 Instance from the class
resource "aws_security_group" "web_ssh" {
  count       = length(var.availability_zones)
  name        = "web-ssh-security-group"
  description = "Allow inbound HTTP, HTTPS, and SSH traffic"
  vpc_id      = var.availability_zones[count.index].vpc_id
  region      = var.availability_zones[count.index].region

  # TODO: Move below out to rules like in the modern docs...
  # Inbound Rules
  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS from anywhere"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH from trusted IP only"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    # BEST PRACTICE: Restrict SSH to your specific IP instead of 0.0.0.0/0
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Outbound Rules (Allow all outbound traffic by default)
  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web-ssh-sg"
  }
}

resource "aws_instance" "webserver" {
  count                       = length(var.availability_zones)
  ami                         = var.availability_zones[count.index].ami_id
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.web_ssh[count.index].id]
  region                      = var.availability_zones[count.index].region
  availability_zone           = var.availability_zones[count.index].az
  user_data                   = file("${path.module}/../.scripts/ec2-user.sh")
  tags = {
    Name = "WebServerExample${var.availability_zones[count.index].az}"
  }
}

# Create a TG for one of the instances
resource "aws_lb_target_group" "demo" {
  name = "demo-tg-route-53"
  port = 80
  protocol = "HTTP"
  region = var.availability_zones[0].region
  vpc_id =  var.availability_zones[0].vpc_id
  deregistration_delay = 30
  target_type = "instance"
}

# Register an instance w/ the tg
resource "aws_lb_target_group_attachment" "demo" {
  target_group_arn = aws_lb_target_group.demo.arn
  target_id = aws_instance.webserver[0].id
  port = 80
  # In order for this to be made the instance needs to exist
  depends_on = [aws_instance.webserver]
}

# Get the public subnets for the vpc
data "aws_subnets" "public" {
  filter {
    name = "vpc-id"
    values = [var.availability_zones[0].vpc_id]
  }

  filter {
    name   = "map-public-ip-on-launch"
    values = ["true"]
  }
}

resource "aws_lb" "demo" {
  name = "DemoRoute53ALB"
  region = var.availability_zones[0].region
  internal = false
  load_balancer_type = "application"
  security_groups = [aws_security_group.web_ssh[0].id]
  subnets = data.aws_subnets.public.ids
}

resource "aws_lb_listener" "demo" {
  load_balancer_arn = aws_lb.demo.arn
  port = 80
  protocol = "HTTP"

  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.demo.arn
  }

  depends_on = [ aws_lb.demo, aws_lb_target_group.demo ]
}

# locals {
#   public_subnets = [
#     for subnet in data.data.aws_subnet.details : subnet
#     if subnet.map
#   ]
# }
