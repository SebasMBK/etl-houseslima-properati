from pydantic import BaseModel, validator

# In this file, lies the code for the data validation to ensure the righ quality before the ingestion
# and after the data cleaning.

class realstate(BaseModel):
    """
    Pydantic model to validate the schema of the extracted files.
    All files extracted should have the same schema, so we only need 1 class.
    """
    id: int
    type: str
    score: float
    title: str
    bedrooms: int
    bathrooms: int
    price: int
    surface: int
    district: str
    geo_lon: float
    geo_lat: float
    place_lon: float
    place_lat: float

    @validator('id')
    def not_null_modelname(cls,id):
        if id == '':
            raise ValueError("id can't be null")
        return id