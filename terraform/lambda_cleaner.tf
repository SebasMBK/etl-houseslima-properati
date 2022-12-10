# This will compress all the files inside the directory "scraper_function"
data "archive_file" "zip_cleaner_files" {
  type        = "zip"
  source_dir  = "../lambda_functions/cleaning_function/"
  output_path = "../lambda_functions/cleaning_function/lambda_cleaner.zip"
}

# This creates the lambda function
resource "aws_lambda_function" "lambda_cleaner" {
  filename      = data.archive_file.zip_cleaner_files.output_path
  function_name = var.lambda_cleaner_name
  role          = aws_iam_role.lambda_role_s3.arn
  layers        = [aws_lambda_layer_version.lambda_layer1.arn]
  handler       = "lambda_cleaner.lambda_handler"
  timeout       = 300
  memory_size   = 512
  architectures = [var.function_arch]
  runtime       = var.function_runtime

  environment {
    variables = {
      raw_bucket_name      = aws_s3_bucket.raw_project_bucket.bucket
      clean_bucket_name    = aws_s3_bucket.clean_project_bucket.bucket
      raw_folder           = var.raw_data_folder
      access_folder        = var.access_data_folder
      raw_data_filename    = var.raw_data_filename
      access_data_filename = var.access_data_filename
    }
  }

  depends_on = [
    aws_cloudwatch_log_group.lambda_cleaner_logs
  ]

}

# This is necessary to allow the creation of a URL
# It is possible to add restrictions to the authorization
resource "aws_lambda_function_url" "lambda_url_cleaner" {
  function_name      = aws_lambda_function.lambda_cleaner.function_name
  authorization_type = "NONE"
}

# Logging
resource "aws_cloudwatch_log_group" "lambda_cleaner_logs" {
  name              = "/aws/lambda/${var.lambda_cleaner_name}"
  retention_in_days = 7
}