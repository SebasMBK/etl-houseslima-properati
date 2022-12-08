FROM ubuntu:22.04
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

# Cleaning the cache
RUN apt-get clean

# Copying the files to the image
WORKDIR /home/project
COPY ./ansible ./ansible
COPY ./terraform ./terraform
COPY ./packages ./packages
COPY ./lambda_functions ./lambda_functions