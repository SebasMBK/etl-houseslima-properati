import pandas as pd
from pandas import DataFrame

def uploader_s3 (clean_bucket_name:str, access_dir:str, access_filename:str ,cleaned_data:dict):
    
    """
    This is a simple function that takes the validated and cleaned data, converts It into a
    DataFrame and finally uploads It directly to our S3 bucket inside a directory where all the 
    access level data is stored.

    Args:
    - clean_bucket_name: Name of the bucket where our clean data is and will be stored.
    - access_dir: Name of the directory inside the bucket where our access level data is stored.
    - cleaned_data: Our cleaned and validated data in form of a dictionary.
    """

    df = pd.DataFrame(cleaned_data)

    # This is to make sure that pandas doesn't overwrite the data type of these 3 columns
    # after removing the null data.
    df['surface'] = df['surface'].astype(int)
    df['bedrooms'] = df['bedrooms'].astype(int)
    df['bathrooms'] = df['bathrooms'].astype(int)
    
    df.to_csv(f"s3://{clean_bucket_name}/{access_dir}/{access_filename}",index=False,encoding='utf-8-sig')