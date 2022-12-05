# This will compress all the files inside the directory "scraper_function"
data "archive_file" "zip_cleaner_files" {
    type = "zip"
    source_dir = "../cleaning_function/"
    output_path = "../cleaning_function/lambda_cleaner.zip"
}

# This creates the lambda function
resource "aws_lambda_function" "lambda_cleaner" {
    filename = data.archive_file.zip_cleaner_files.output_path
    function_name = var.lambda_cleaner_name
    role = aws_iam_role.lambda_role_s3.arn
    layers = [aws_lambda_layer_version.lambda_layer.arn]
    handler = "lambda_cleaner.lambda_handler"
    timeout = 300
    memory_size = 512
    architectures = [var.function_arch]
    runtime = var.function_runtime

    environment {
      variables = {
        bucket_name = aws_s3_bucket.project_bucket.bucket
        raw_folder = var.raw_data_folder
        access_folder = var.access_data_folder
      }
    }
}

# This is necessary to allow the creation of a URL
# It is possible to add restrictions to the authorization
resource "aws_lambda_function_url" "lambda_url_cleaner" {
  function_name      = aws_lambda_function.lambda_cleaner.function_name
  authorization_type = "NONE"
}