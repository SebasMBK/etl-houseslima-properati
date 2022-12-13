FROM ubuntu:22.04
# This "ARG" is necessary to bypass the bug where the ansible installation will you ask to insert
# some geopraphic information stopping the process.
ARG DEBIAN_FRONTEND=noninteractive
USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get autoremove -yqq --purge \
    && apt-get -y install libpq-dev gcc \
    && apt-get install -y wget \
    && apt-get install -y curl \
    && apt-get install -y zip unzip

# Installing Terraform
    # Ensure System is up to date
RUN apt-get install -y gnupg software-properties-common \
    # Install HashiCorp GPG Key
    && wget -O- https://apt.releases.hashicorp.com/gpg | \
       gpg --dearmor | \
       tee /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    # Verify the key's fingerprint
    && gpg --no-default-keyring \
       --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
       --fingerprint \
    # Add HashiCorp repo to the system
    && echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
       https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
       tee /etc/apt/sources.list.d/hashicorp.list \
    # Download the package information
    && apt update \
    # Install terraform
    && apt-get install -y terraform

# This will install the AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install
    
# Installing Ansible
RUN apt install software-properties-common \
    # boto3 is necessary for the Ansible aws plugin
    && apt install python3-boto3 -y \
    && apt-add-repository --yes --update ppa:ansible/ansible \
    && apt install ansible -y


# Cleaning the cache
RUN apt-get clean

# Copying the files to the image
WORKDIR /home/project
COPY ./ansible ./ansible
COPY ./terraform ./terraform
COPY ./packages ./packages
COPY ./lambda_functions ./lambda_functions
COPY run_pipeline.sh ./run_pipeline.sh