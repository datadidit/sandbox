output "home_ip" {
  description = "IP of your local workstation"
  value       = data.http.my_public_ip.response_body
}

output "home_sg" {
    description = "Reference to the home security group"
    value = {
        arn = aws_security_group.ssh_restricted.arn
        id = aws_security_group.ssh_restricted.id
    }
}

output "ec2_info" {
    value = aws_instance.ec2_instance
}

output "ssh_command" {
    description = "SSH Command you can run to access the image"
    value = "ssh ec2-user@${aws_instance.ec2_instance.public_dns}"
}