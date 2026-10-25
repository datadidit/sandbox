variable "aws_profile_name" {
  description = "Name of your local aws profile"
  type        = string
}

variable "ami_id" {
    description = "The ID of the AMI"
    type = string
    default = "ami-08c46876c64a927b8"
}