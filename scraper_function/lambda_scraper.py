import json
from data_scraper import data_scraper
from uploader_s3 import uploader_s3
import os

def lambda_handler(event, context):
    
    # Getting env variables passed when creating the lambda function with terraform
    bucket_name = os.environ['bucket_name']
    raw_folder = os.environ['raw_folder']

    df = data_scraper(nr_pages=1)

    uploader_s3(bucket_name=bucket_name,
                raw_folder=raw_folder,
                filename="raw_real_state",
                df=df
                )
    
    return {
        "statusCode":200,
        "body":json.dumps("Data extracted and uploaded succesfully")
    }