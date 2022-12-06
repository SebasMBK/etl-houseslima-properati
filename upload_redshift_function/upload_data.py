import redshift_connector

def upload_to_staging(
    host:str,
    database:str,
    user:str,
    password:str,
    bucket_name:str,
    access_folder:str,
    access_data_filename:str,
    staging_table:str,
    iam_role_arn:str
):

    with redshift_connector.connect(

        host=host,
        database=database,
        user=user,
        password=password

    ) as conn:
    
        conn.autocommit = True

        with conn.cursor() as cursor:

            cursor.execute(f"""

            COPY {staging_table} FROM 's3://{bucket_name}/{access_folder}/{access_data_filename}'
            CREDENTIALS 'aws_iam_role={iam_role_arn}' IGNOREHEADER 1 DELIMITER ',' CSV;

            """)

def upload_to_main(
    host:str,
    database:str,
    user:str,
    password:str,
    main_table:str,
    staging_table:str
):

    with redshift_connector.connect(

        host=host,
        database=database,
        user=user,
        password=password

    ) as conn:
    
        conn.autocommit = True

        with conn.cursor() as cursor:
            

            cursor.execute(f"""

            INSERT INTO {main_table}
            
            (SELECT s_tbl.id, s_tbl.type, s_tbl.score, s_tbl.title, s_tbl.bedrooms, s_tbl.bathrooms, s_tbl.price, s_tbl.surface, s_tbl.district, s_tbl.geo_lon, s_tbl.geo_lat, s_tbl.place_lon, s_tbl.place_lat
             FROM {staging_table} s_tbl
             LEFT OUTER JOIN {main_table} m_tbl ON
             s_tbl.id = m_tbl.id
             WHERE m_tbl.id IS NULL
             )
            
            """)
            

            cursor.execute(f"""

            UPDATE {main_table} m_tbl
            SET score = s_tbl.score, title = s_tbl.title, price = s_tbl.price
            FROM {staging_table} s_tbl
            WHERE m_tbl.id = s_tbl.id;
            
            """)
            
            
            cursor.execute(f"""
            
            DROP TABLE {staging_table}
            
            """)