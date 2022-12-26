#!/bin/bash
#This file is only for running inside the docker container.
#This will ask for you AWS keys
aws configure
#The next 2 lines of code starts terraform and creates the Infra
terraform -chdir=/home/project/terraform init
terraform -chdir=/home/project/terraform apply
#This will give the right permissions to the ec2key for the ec2instance where our web application 
#will be hosted
chmod 400 /home/project/ansible/ec2key