import json
from data_scraper import data_scraper
from uploader_s3 import uploader_s3
import os

def lambda_handler(event, context):
    
    # Getting env variables passed when creating the lambda function with terraform
    raw_bucket_name = os.environ['raw_bucket_name']
    raw_folder = os.environ['raw_folder']
    raw_filename = os.environ['raw_data_filename']


    df = data_scraper(nr_pages=20)

    uploader_s3(raw_bucket_name=raw_bucket_name,
                raw_folder=raw_folder,
                raw_filename=raw_filename,
                df=df
                )
    
    return {
        "statusCode":200,
        "body":json.dumps("Data extracted and uploaded succesfully")
    }