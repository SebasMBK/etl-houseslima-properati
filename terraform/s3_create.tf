resource "aws_s3_bucket" "project_bucket" {
    bucket = var.bucket_name
    force_destroy = true
}

resource "aws_s3_bucket_versioning" "bucket_versioning" {
    bucket = aws_s3_bucket.project_bucket.id
    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_s3_bucket" "packages_bucket" {
    bucket = var.packages_bucket_name
    force_destroy = true
}

resource "aws_s3_bucket_versioning" "packages_bucket_versioning" {
    bucket = aws_s3_bucket.packages_bucket.id
    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_s3_object" "packages" {
    bucket = aws_s3_bucket.packages_bucket.bucket
    key = "packages.zip"
    source = "../packages/lambdapackages.zip"
}

