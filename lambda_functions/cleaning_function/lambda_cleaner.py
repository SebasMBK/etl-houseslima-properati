from data_cleaner import data_cleaner
from uploader_s3 import uploader_s3
from pydantic import ValidationError
from model_pydantic import realstate
import os
import json

def lambda_handler(event, context):
    
    # Getting env variables passed when creating the lambda function with terraform
    raw_bucket_name = os.environ['raw_bucket_name']
    raw_dir = os.environ['raw_folder']
    access_folder =  os.environ['access_folder']
    raw_filename = os.environ['raw_data_filename']
    clean_bucket_name = os.environ['clean_bucket_name']
    access_filename = os.environ['access_data_filename']


    access_level_data = data_cleaner(raw_bucket_name=raw_bucket_name, raw_dir=raw_dir, raw_filename=raw_filename)

    try:    

        validated_file = [realstate.parse_obj(data_) for data_ in access_level_data]
        uploader_s3(clean_bucket_name=clean_bucket_name, access_dir=access_folder, access_filename=access_filename, cleaned_data=access_level_data)

        return {
        "statusCode":200,
        "body":json.dumps("Data cleaned, validated and uploaded")
    }

    except ValidationError as e:
    
        return {
            "statusCode":400,
            "body":json.dumps(f"Error validating data: {e}")
        }
