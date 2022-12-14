terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    awslightsail = {
      source = "DeYoungTech/awslightsail"
      version = "0.7.0"
    }
  }
}

provider "aws" {
  region = var.project_region
}

provider "awslightsail" {
  region = var.project_region
}