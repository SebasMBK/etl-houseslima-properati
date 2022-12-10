# This resource is necessary for scheduling the pipeline
resource "aws_cloudwatch_event_rule" "step_functions_schedule" {
  name                = "schedule_pipeline"
  description         = "Schedule AWS Step Functions containing Lambda functions"
  schedule_expression = "rate(2 minutes)"
  role_arn            = aws_iam_role.eventbridge_role.arn

}

resource "aws_cloudwatch_event_target" "step_functions_target" {
  rule      = aws_cloudwatch_event_rule.step_functions_schedule.name
  target_id = "sendEventToStepFunctions"
  arn       = aws_sfn_state_machine.step_functions.arn
  role_arn  = aws_iam_role.eventbridge_role.arn

}