# This executes the command that will build our locally created docker image
resource "null_resource" "create-properati-image" {
  provisioner "local-exec" {

    command = "docker build -t ${var.docker_image_name} ."
    working_dir = "../flask_api/"
  
  }
}

resource "awslightsail_container_service" "lightsail_container" {
  name        = var.container_service_name
  power       = "micro"
  scale       = 1
  is_disabled = false

  depends_on = [
    null_resource.create-properati-image
  ]
}

# This command will push our locally created docker image to Lightsail continers repository
resource "null_resource" "push-properati-image-to-lightsail" {
  provisioner "local-exec" {

    command = "aws lightsail push-container-image --service-name ${var.container_service_name} --label ${var.container_flag} --region ${var.project_region} --image ${var.docker_image_name}"
    working_dir = "../flask_api/"
  }

  depends_on = [
    awslightsail_container_service.lightsail_container
  ]
}

# This deploys the container
resource "awslightsail_container_deployment" "flask_api_container" {
  container_service_name = awslightsail_container_service.lightsail_container.id
  container {
    container_name = var.container_service_name
    image          = ":${var.container_service_name}.${var.container_flag}.latest"

    port {
      port_number = 80
      protocol    = "HTTP"
    }

    environment {
      key = "DATABASE_URL"
      value = "postgresql://${var.redshift_user}:${var.redshift_pass}@${aws_redshift_cluster.realstate_cluster.endpoint}/${var.redshift_dbname}"
    }
  }

  public_endpoint {
    container_name = var.container_service_name
    container_port = 80

    health_check {
      healthy_threshold   = 2
      unhealthy_threshold = 2
      timeout_seconds     = 2
      interval_seconds    = 5
      path                = "/"
      success_codes       = "200-499"
    }
  }

  depends_on = [
    null_resource.push-properati-image-to-lightsail
  ]

}