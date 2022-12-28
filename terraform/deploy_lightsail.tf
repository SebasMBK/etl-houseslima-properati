resource "awslightsail_container_service" "lightsail_container" {
  name        = var.container_service_name
  power       = "micro"
  scale       = 1
  is_disabled = false
}

# This file will be used to deploy the Flask API APP inside the container
resource "local_file" "containers_json" {
  content  = <<EOF
{
    "${var.container_service_name}": {
        "image": ":${var.container_service_name}.${var.container_flag}.1",
        "ports": {
            "5000": "HTTP"
        },
        "environment": {
                "redshift_user":"${var.redshift_user}",
                "redshift_pass":"${var.redshift_pass}",
                "redshift_database":"${var.redshift_dbname}",
                "redshift_host":"${aws_redshift_cluster.realstate_cluster.endpoint}",
                "redshift_port":"${aws_redshift_cluster.realstate_cluster.port}",
                "DATABASE_URL":"postgresql://${var.redshift_user}:${var.redshift_pass}@${aws_redshift_cluster.realstate_cluster.endpoint}/${var.redshift_dbname}"
        }
    }
}
EOF
  filename = "../flask_api/containers.json"
}

# This file will be used to create a public endpoint to the container
resource "local_file" "public_endpoint_json" {
  content  = <<EOF
{
    "containerName": "${var.container_service_name}",
    "containerPort": 5000
}
EOF
  filename = "../flask_api/public-endpoint.json"
}

# This will create the file that indicates what commands we will be running to deploy
# the lightsail container
resource "local_file" "deploy_commands" {
  content  = <<EOF
1. docker build -t ${var.docker_image_name} .
2. aws lightsail push-container-image --service-name ${var.container_service_name} --label ${var.container_flag} --region ${var.project_region} --image ${var.docker_image_name}
3. aws lightsail create-container-service-deployment --service-name ${var.container_service_name} --containers file://containers.json --public-endpoint file://public-endpoint.json
EOF
  filename = "../flask_api/deploy_commands.txt"
}