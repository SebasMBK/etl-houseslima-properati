#!/bin/bash
#This file is only for running inside the docker container.
aws configure
terraform -chdir=/home/project/terraform init
terraform -chdir=/home/project/terraform apply
chmod 400 /home/project/ansible/ec2key
cd /home/project/ansible && ansible-playbook playbook.yml