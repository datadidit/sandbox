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