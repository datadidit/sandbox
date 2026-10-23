output "web_endpoints" {
  description = "List of ssh commands for the instances you've created"
  value       = [for instance in aws_instance.webserver : "http://${instance.public_dns}"]
}