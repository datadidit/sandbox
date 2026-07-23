variable "aws_profile_name" {
  description = "Name of your local aws profile"
  type        = string
}

variable "aws_key_pair_name" {
    description = "Name of your AWS key pair that will be used for ssh"
    type = string
}

# TODO: Make this work...
# variable "aws_ami_name_filter" {
#     description = "Filter for finding the hvm ami"
#     type = list(string)
#     default = ["ubuntu/images/hvm-ssd/ubuntu-resolute-26.04-amd64-server-*"]
# }

variable "aws_ami_image_id" {
    description = "image id for the ami."
    type = string
    default = "ami-0b6d9d3d33ba97d99"
}

variable "aws_instance_type" {
    description = "Size of the image to stand up"
    type = string
    default = "t3a.nano"
}

variable "aws_additional_security_groups" {
    description = "Additional security groups on top of the ssh only one created by module"
    type = list(string)
    default = []
}

variable "aws_instance_startup_script" {
    description = "Startup script for instance."
    type = string
    default = null
}