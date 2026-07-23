output "home_ip" {
  description = "IP of your local workstation"
  value       = data.http.my_public_ip.body
}