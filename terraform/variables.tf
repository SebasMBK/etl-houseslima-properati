variable "project_region" {
    type = string
    default = "us-east-1"
}

variable "bucket_name" {
    type = string
    default = "realstatelima"
}

variable "packages_bucket_name" {
    type = string
    default = "lambdalayerspackages"
}

variable "raw_data_folder" {
    type = string
    default = "rawdata"
}

variable "access_data_folder" {
    type = string
    default = "accessdata"
}

variable "lambda_scraper_name" {
    type = string
    default = "data_scraping"
}

variable "lambda_cleaner_name" {
    type = string
    default = "data_cleaning"
}

variable "function_runtime" {
    type = string
    default = "python3.9"
}

variable "function_arch" {
    type = string
    default = "x86_64"
}

variable "redshift_user" {
    type = string
    description = "User for Redshift"
}

variable "redshift_pass" {
    type = string
    description = "Password for Redshift"
}

variable "redshift_dbname" {
    type = string
    default = "realstatelima"
}

variable "redshift_cluster" {
    type = string
    default = "realstate-lima-cluster"
}
