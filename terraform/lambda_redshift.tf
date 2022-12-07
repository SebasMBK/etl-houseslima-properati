# This will compress all the files inside the directory "scraper_function"
data "archive_file" "zip_redshift_files" {
    type = "zip"
    source_dir = "../upload_redshift_function/"
    output_path = "../upload_redshift_function/lambda_redshift.zip"
}

# This creates the lambda function
resource "aws_lambda_function" "lambda_redshift" {
    filename = data.archive_file.zip_redshift_files.output_path
    function_name = var.lambda_redshift_name
    role = aws_iam_role.lambda_role_s3.arn
    layers = [aws_lambda_layer_version.lambda_layer2.arn]
    handler = "lambda_redshift.lambda_handler"
    timeout = 300
    memory_size = 512
    architectures = [var.function_arch]
    runtime = var.function_runtime

    environment {
      variables = {
        clean_bucket_name = aws_s3_bucket.clean_project_bucket.bucket
        access_folder = var.access_data_folder
        access_data_filename = var.access_data_filename
        database = aws_redshift_cluster.realstate_cluster.database_name
        username = aws_redshift_cluster.realstate_cluster.master_username
        password = aws_redshift_cluster.realstate_cluster.master_password
        endpoint = aws_redshift_cluster.realstate_cluster.endpoint
        role_arn = aws_iam_role.project_redshift_role.arn
      }
    }
}

# This is necessary to allow the creation of a URL
# It is possible to add restrictions to the authorization
resource "aws_lambda_function_url" "lambda_url_redshift" {
  function_name      = aws_lambda_function.lambda_redshift.function_name
  authorization_type = "NONE"
}