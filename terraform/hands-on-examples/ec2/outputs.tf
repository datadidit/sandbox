output "http_endpoint" {
    description = "Where you can see the hello world endpoint"
    value = "http://${aws_instance.webserver.public_dns}"
}