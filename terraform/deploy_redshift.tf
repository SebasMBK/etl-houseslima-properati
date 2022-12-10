resource "aws_redshift_cluster" "realstate_cluster" {
  cluster_identifier = var.redshift_cluster
  database_name      = var.redshift_dbname
  master_username    = var.redshift_user
  master_password    = var.redshift_pass
  node_type          = "dc2.large"
  cluster_type       = "single-node"

  iam_roles                           = [aws_iam_role.project_redshift_role.arn]
  skip_final_snapshot                 = true
  publicly_accessible                 = true
  automated_snapshot_retention_period = 0
  vpc_security_group_ids              = [aws_security_group.project_security_group.id]

  # Logging
  logging {
    enable               = true
    log_destination_type = "cloudwatch"
    log_exports          = ["connectionlog", "userlog", "useractivitylog"]
  }

}