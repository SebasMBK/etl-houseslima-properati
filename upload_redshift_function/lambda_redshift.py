from create_tables import create_table_main
from create_tables import create_table_staging
import json
import os

def lambda_handler(event, context):
    
    # Getting env variables passed when creating the lambda function with terraform
    bucket_name = os.environ['bucket_name']
    access_folder = os.environ['access_folder']
    access_data_filename = os.environ['access_data_filename']
    host = os.environ['endpoint'].split(":")[0]
    database = os.environ['database']
    user = os.environ['username']
    password = os.environ['password']
    

    create_table_main(host=host, database=database, user=user, password=password)
    create_table_staging(host=host, database=database, user=user, password=password)
    
    return {
        "statusCode":200,
        "body":json.dumps("Data uploaded to redshift successfully")
    }