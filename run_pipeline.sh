#!/bin/bash
#This file is only for running inside the docker container.
#This will ask for you AWS keys
aws configure
#The next 3 lines of code starts terraform and creates the Infra
terraform -chdir=/home/project/terraform init
terraform -chdir=/home/project/terraform apply
chmod 400 /home/project/ansible/ec2key