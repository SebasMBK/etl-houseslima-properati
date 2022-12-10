resource "aws_s3_bucket" "raw_project_bucket" {
  bucket        = var.raw_bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "raw_bucket_versioning" {
  bucket = aws_s3_bucket.raw_project_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket" "clean_project_bucket" {
  bucket        = var.clean_bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "clean_bucket_versioning" {
  bucket = aws_s3_bucket.clean_project_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket" "packages_bucket" {
  bucket        = var.packages_bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "packages_bucket_versioning" {
  bucket = aws_s3_bucket.packages_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_object" "packages1" {
  bucket = aws_s3_bucket.packages_bucket.bucket
  key    = "packages1.zip"
  source = "../packages/packages1.zip"
}

resource "aws_s3_object" "packages2" {
  bucket = aws_s3_bucket.packages_bucket.bucket
  key    = "packages2.zip"
  source = "../packages/packages2.zip"
}


