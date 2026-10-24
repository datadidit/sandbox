output "web_endpoints" {
  description = "List of ssh commands for the instances you've created"
  value       = [for instance in aws_instance.webserver : "http://${instance.public_dns}"]
}

output "target_group" {
    description = "Information on where to find the target group"
    value = "Target group is in ${var.availability_zones[0].region} w/ name ${aws_lb_target_group.demo.name}"
}

output "public_subnets" {
    description = "The public subnets for index 0"
    value = "These are the public subnets for ${var.availability_zones[0].vpc_id} ${jsonencode(data.aws_subnets.public.ids)}"
}

output "aws_lb" {
    description = "DNS of the ALB"
    value = "http://${aws_lb.demo.dns_name}"
}