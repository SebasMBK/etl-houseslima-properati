import pandas as pd

def data_cleaner(bucket_name:str, raw_dir:str):

    """
    This function takes the extracted data in It's raw format and cleans it.
    This function returns a dictionary.

    Args:
    - bucket_name: Name of the bucket where our data Is and Will be stored.
    - raw_dir: Name of the directory inside the bucket where our raw data is stored.
    """

    # Reading the csv directly from our s3 bucket
    df = pd.read_csv(f's3://{bucket_name}/{raw_dir}/raw_real_state.csv')

    # Data must have Geo location and/or Place location. Both can't be null
    df.dropna(subset=['geo_point.lon','place.lon'], how='all', inplace=True)

    # Changing the names of the columns
    df.rename(
            columns=
                {'floor_plan.bedrooms':'bedrooms',
                'floor_plan.bathrooms':'bathrooms',
                'price.amount':'price',
                'surface.total':'surface',
                'place.short_name':'district',
                'geo_point.lon':'geo_lon',
                'geo_point.lat':'geo_lat',
                'place.lon':'place_lon',
                'place.lat':'place_lat'
            }, inplace=True
    )

    return df.to_dict("records")