#!/bin/bash
#This will run the ansible playbook that will start the streamlit application
#inside the ec2 instance
cd /home/project/ansible && ansible-playbook playbook.yml