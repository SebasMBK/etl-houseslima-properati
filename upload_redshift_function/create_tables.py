import redshift_connector

def create_table_main(host:str, database:str, user:str, password:str):

    with redshift_connector.connect(

        host=host,
        database=database,
        user=user,
        password=password

    ) as conn:
    
        conn.autocommit = True

        with conn.cursor() as cursor:

            cursor.execute("""

            CREATE TABLE IF NOT EXISTS realstatedata (
            id INT NOT NULL PRIMARY KEY,
            type VARCHAR(100),
            score NUMERIC(8,7),
            title VARCHAR(255),
            bedrooms INT,
            bathrooms INT,
            price INT,
            surface INT,
            district VARCHAR(100),
            geo_lon NUMERIC (5,3),
            geo_lat NUMERIC (5,3),
            place_lon NUMERIC (5,3),
            place_lat NUMERIC (5,3)
            );

            """)
            

def create_table_staging(host,database,user,password):

    with redshift_connector.connect(

        host=host,
        database=database,
        user=user,
        password=password

    ) as conn:
    
        conn.autocommit = True

        with conn.cursor() as cursor:
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS realstatedata_staging (LIKE realstatedata);
            """)