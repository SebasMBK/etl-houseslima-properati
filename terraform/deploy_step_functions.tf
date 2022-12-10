resource "aws_sfn_state_machine" "step_functions" {
  name     = "project_state_machine"
  role_arn = aws_iam_role.step_functions_role.arn

  definition = <<EOF
{
  "Comment": "Function to invoke all tasks from the pipeline",
  "StartAt": "datascraper",
  "States": {
    "datascraper": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_scraping.arn}",
      "Retry": [
        {
          "ErrorEquals": [
            "Lambda.ServiceException",
            "Lambda.AWSLambdaException",
            "Lambda.SdkClientException",
            "Lambda.TooManyRequestsException"
          ],
          "IntervalSeconds": 2,
          "MaxAttempts": 2,
          "BackoffRate": 2
        }
      ],
      "Next": "datacleaner"
    },
    "datacleaner": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_cleaner.arn}",
      "Retry": [
        {
          "ErrorEquals": [
            "Lambda.ServiceException",
            "Lambda.AWSLambdaException",
            "Lambda.SdkClientException",
            "Lambda.TooManyRequestsException"
          ],
          "IntervalSeconds": 2,
          "MaxAttempts": 2,
          "BackoffRate": 2
        }
      ],
      "Next": "redshiftupload"
    },
    "redshiftupload": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_redshift.arn}",
      "Retry": [
        {
          "ErrorEquals": [
            "Lambda.ServiceException",
            "Lambda.AWSLambdaException",
            "Lambda.SdkClientException",
            "Lambda.TooManyRequestsException"
          ],
          "IntervalSeconds": 2,
          "MaxAttempts": 2,
          "BackoffRate": 2
        }
      ],
      "End": true
    }
  }
}
EOF

  logging_configuration {
    log_destination        = "${aws_cloudwatch_log_group.stepfunctions_logs.arn}:*"
    include_execution_data = true
    level                  = "ALL"
  }

}

# Logging
resource "aws_cloudwatch_log_group" "stepfunctions_logs" {
  name              = "/aws/states/project_state_machine"
  retention_in_days = 7
}