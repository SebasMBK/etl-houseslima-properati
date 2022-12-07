import boto3
from pandas import DataFrame
from io import StringIO

def uploader_s3(raw_bucket_name:str, raw_folder:str, raw_filename:str, df:DataFrame):
    
    """
    This function takes a dataframe, converts It in a csv file, saves that file in the buffer and then uploads to S3.
    
    Args:
    - raw_bucket_name: Name of the bucket where our extracted data will be stored.
    - raw_folder: Name of the folder where the raw data will be uploaded
    - raw_filename: Name of the csv file that contains the raw data
      example -> real_state_file
    - df: DataFrame to be uploaded to S3.
    """

    bucket = raw_bucket_name
    csv_buffer = StringIO()
    df.to_csv(csv_buffer,index=False,encoding="utf-8-sig")
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, f'{raw_folder}/{raw_filename}').put(Body=csv_buffer.getvalue())