# #!/usr/bin/env python
# # coding: utf-8

# import pandas as pd
# from sqlalchemy import create_engine
# from tqdm.auto import tqdm


# dtype = {
#     "VendorID": "Int64",
#     "passenger_count": "Int64",
#     "trip_distance": "float64",
#     "RatecodeID": "Int64",
#     "store_and_fwd_flag": "string",
#     "PULocationID": "Int64",
#     "DOLocationID": "Int64",
#     "payment_type": "Int64",
#     "fare_amount": "float64",
#     "extra": "float64",
#     "mta_tax": "float64",
#     "tip_amount": "float64",
#     "tolls_amount": "float64",
#     "improvement_surcharge": "float64",
#     "total_amount": "float64",
#     "congestion_surcharge": "float64"
# }

# parse_dates = [
#     "tpep_pickup_datetime",
#     "tpep_dropoff_datetime"
# ]


# prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
# url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'

# # from sqlalchemy import create_engine
# engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

# df.head()

# df.dtypes

# from sqlalchemy import create_engine
# engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# # df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

# def run():
#     pg_user="root"
#     pg_password="root"
#     pg_host="localhost"
#     pg_port=5432
#     pg_db="ny_taxi"

#     year=2021
#     month=1
#     target_table  = "yellow_taxi_data"
    
    
#     chunk_size = 100000
    
#     df_iter = pd.read_csv(
#         url,
#         dtype=dtype,
#         parse_dates=parse_dates,
#         iterator=True,
#         chunksize=chunk_size
#     )

#     first=True
#     for df_chunk in tqdm(df_iter):
#         if first:
#             df_chunk.head(n=0).to_sql(
#     target_table  = "yellow_taxi_data"
#                 name=target_table, con=engine, if_exists='replace')
#             first=False
#         df_chunk.to_sql(name=target_table, con=engine, if_exists='append')



#     df_iter = pd.read_csv(
#         url,
#         dtype=dtype,
#         parse_dates=parse_dates,
#         iterator=True,
#         chunksize=chunk_size
#     )

#     for df_chunk in tqdm(df_iter):
#         df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
#         # print(len(df_chunk))



#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


# -----------------------------
# Data types
# -----------------------------
dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


# -----------------------------
# Main function
# -----------------------------
def run():

    # PostgreSQL configuration
    pg_user = "root"
    pg_password = "root"
    pg_host = "localhost"
    pg_port = 5432
    pg_db = "ny_taxi"

    # Dataset
    year = 2021
    month = 1

    target_table = "yellow_taxi_data"

    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow"

    url = f"{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz"

    print(f"Downloading data from:\n{url}\n")

    # Create database engine
    engine = create_engine(
        f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"
    )

    # Read CSV in chunks
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=100000
    )

    first = True

    # Insert into PostgreSQL
    for df_chunk in tqdm(df_iter):

        if first:
            df_chunk.head(0).to_sql(
                name=target_table,
                con=engine,
                if_exists="replace",
                index=False
            )
            first = False

        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False
        )

    print("\nData loaded successfully!")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    run()
