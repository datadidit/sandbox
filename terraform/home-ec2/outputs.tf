# output "home_ip" {
#   description = "IP of your local workstation"
#   value       = data.http.my_public_ip.response_body
# }

# TODO: Bring this back once you add the user on your own.
# output "local_os_username" {
#   value = data.external.local_user.result["user"]
# }

output "ssh_command" {
  description = "SSH Command you can run to access the image"
  value       = "ssh ${local.default_user}@${aws_instance.ec2_instance.public_dns}"
}