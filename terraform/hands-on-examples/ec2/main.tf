# Create the Webserver EC2 Instance from the class
data "aws_vpc" "default" {
  default = true
}

resource "aws_security_group" "web_ssh" {
  name        = "web-ssh-security-group"
  description = "Allow inbound HTTP, HTTPS, and SSH traffic"
  vpc_id      = data.aws_vpc.default.id

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
    ami = var.ami_id
    instance_type = "t2.micro"
    user_data = file("${path.module}/../.scripts/ec2-user-data.sh")
    vpc_security_group_ids = [aws_security_group.web_ssh.id]
    tags = { 
        Name = "WebServerExample"
    }
}

# TODO: Add a wait for the endpoint to actually be available