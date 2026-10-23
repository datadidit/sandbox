variable "aws_profile_name" {
  description = "Name of your local aws profile"
  type        = string
}

variable "availability_zones" {
  type = list(object({
    region = string
    az     = string
    ami_id = string
    vpc_id = string
  }))
  description = "List of 3 region - az pairs to create EC2 instances in."

  validation {
    condition     = length(var.availability_zones) <= 3
    error_message = "The availability zones cannot contain more than 3 items"
  }
}