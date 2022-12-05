# This will take the compressed file with all the necessary packages an take it to lambda
resource "aws_lambda_layer_version" "lambda_layer" {
  s3_bucket = aws_s3_bucket.packages_bucket.bucket
  s3_key = aws_s3_object.packages.key
  layer_name = "packages_layer_lambda"

  compatible_runtimes = [var.function_runtime]
  compatible_architectures = [var.function_arch]
}