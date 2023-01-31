# ETL-Houseslima-Properati

This project creates a pipeline that takes data from [Properati](https://www.properati.com.pe/) web page (
Properati is a real estate search site), processes it using lambda functions and, finally, stores it in a redshift database. This pipeline is orchestrated using AWS Step Functions and scheduled with AWS EventBridge.
Also, we'll build a FLASK REST API to interact with the database. This Flask App allow us to retrieve data and is hosted in AWS Lightsail container service.

The tools that were used for the project are:
- [AWS](https://aws.amazon.com/) for hosting the infraestructure.
- [AWS S3](https://aws.amazon.com/es/s3/) as our storage.
- [AWS Lambda](https://aws.amazon.com/es/lambda/) as the executor.
- [AWS Redshift](https://aws.amazon.com/redshift/) as our data warehouse.
- [AWS Step Functions](https://aws.amazon.com/step-functions/?nc1=h_ls) for orchestrating our pipeline.
- [AWS Eventbrigde](https://aws.amazon.com/eventbridge/) for scheduling our pipeline.
- [AWS Lightsail Containers](https://aws.amazon.com/es/lightsail/) for hosting our Flask REST API App.
- [Terraform](https://www.terraform.io/) as IaC for the infra provisioning.
- [Docker](https://www.docker.com/) for containerizing our FLASK APP.
- [Insomnia](https://insomnia.rest/) and [Flask](https://flask.palletsprojects.com/en/2.2.x/) for testing and developing our REST API.
- [pytest] (https://docs.pytest.org/en/7.2.x/) for testing the response we recieve from the webpage.
- [Python](https://www.python.org/) as the main programming language.

## Project's Architecture

![project_arch](https://github.com/SebasMBK/etl-houseslima-properati/blob/master/images/aws_arch.png) 

1. Extracting data from [Properati](https://www.properati.com.pe/)
2. The extracted data is validated, cleaned and uploaded to redshift.
3. A Flask REST API is created for the database so we can interact with the data inside our Data Warehouse.
4. Users can now analyze the data using any visualization tool they prefer or use the API to develop new solutions.

## Project's requirements
These next requirements need to be installed locally for the correct functioning of the solution:
1. [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) for account configuring and terraform provisioning.
2. [AWS CLI Lighstail plugin](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software) for deploying our containers and pushing the docker images to the AWS Lightsail Containers' Repository.
3. [Terraform](https://www.terraform.io/) to provision the infraestructure.
4. [Docker](https://www.docker.com/) to containerize the Flask REST API App image.

## Start Pipeline
For testing, let's go to our root folder and run: 

`pytest`: This will run some tests to make sure the web page works as we want to. 
1. The first test will make sure that we recieve the response 200, meaning that the webpage exists and we have access to it.
2. The second test will make sure that the limit of elements per page is 30. 
          
Now to create the pipeline, terraform will initialize everything that we need. Just clone the repo and execute the next commands inside the terraform folder: 
1.  `aws configure`: This command is used to login into an AWS Account using your secret access keys. 
2.  `terraform init`: This will initiate terraform in the folder.
3.  `terraform apply`: This will create our infraestructure. You will be prompt to input a redshift password and user. 
4.  (Only run if you want to destroy the infraestructure) `terraform destroy`: This destroys the created infraestructure. 

This pipeline is scheduled hourly, so we can wait 1 hour for the pipeline to run or run our Step Functions' State Machines manually.

## Flask REST API
|Path|Request Type| Parameters|
|---|---|---|
|`/properties`| GET| No parameters required. This request retrieves all the data from our database.|
|`/properties`| POST| id(int), type(str), score(int), title(str), bedrooms(int), bathrooms(int), price(int), surface(int), district(str), geo_lon(float), geo_lat(float), place_lon(float), place_lat(float)|
|`/properties/<int:id>`| GET| No parameters required. This request retrieves an specific property from our database by its id.|

- The Flask API URL can be found in the AWS lightsail container service.
- The path URL/swagger-ui will show the documentation of the Flask API.
