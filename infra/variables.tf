variable "aws_region" {
  default = "ap-south-1"
}

variable "project_name" {
  default = "rohan-taskapi"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  default = ["10.0.3.0/24", "10.0.4.0/24"]
}
variable "db_password" {
  type      = string
  sensitive = true
  default   = "ChangeMe123!"
}

variable "ecr_image_url" {
  type    = string
  default = "public.ecr.aws/nginx/nginx:latest"
}