from create_tables import create_table_main
from create_tables import create_table_staging
from upload_data import upload_to_main
from upload_data import upload_to_staging
import json
import os

def lambda_handler(event, context):
    
    # Getting env variables passed when creating the lambda function with terraform
    clean_bucket_name = os.environ['clean_bucket_name']
    access_folder = os.environ['access_folder']
    access_data_filename = os.environ['access_data_filename']
    host = os.environ['endpoint'].split(":")[0]
    database = os.environ['database']
    user = os.environ['username']
    password = os.environ['password']
    iam_role_arn = os.environ['role_arn']
    main_table = "realstatedata"
    staging_table = "realstatedata_staging"
    

    create_table_main(
        host=host,
        database=database,
        user=user,
        password=password,
        main_table=main_table
    )

    create_table_staging(
        host=host,
        database=database,
        user=user,
        password=password,
        main_table=main_table,
        staging_table=staging_table
    )

    upload_to_staging(
        host=host,
        database=database,
        user=user,
        password=password,
        clean_bucket_name=clean_bucket_name,
        access_folder=access_folder,
        access_data_filename=access_data_filename,
        staging_table=staging_table,
        iam_role_arn=iam_role_arn
    )

    upload_to_main(
        host=host,
        database=database,
        user=user,
        password=password,
        main_table=main_table,
        staging_table=staging_table
    )
    
    return {
        "statusCode":200,
        "body":json.dumps("Data uploaded to redshift successfully")
    }