import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
RAW_DATA_DIR = PROJECT_ROOT / "raw_dataset"#
CLEANED_DATA_DIR = PROJECT_ROOT / "cleaned_dataset"

dim_business = pd.read_csv(CLEANED_DATA_DIR/'dim_business.csv')
dim_rider = pd.read_csv(CLEANED_DATA_DIR/'dim_rider.csv')
dim_flour_type = pd.read_csv(CLEANED_DATA_DIR/'dim_flour_type.csv')
orders_fact = pd.read_csv(CLEANED_DATA_DIR/'orders_fact.csv')

print('csv files loaded sucessfully')

db_name = 'flour4four'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'


def get_connection():
    connection = psycopg2.connect(dbname = db_name,
                                  user = user,
                                  password = password,
                                  host = host,
                                  port = port)
    return connection



def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    table_query = '''CREATE SCHEMA IF NOT EXISTS flour;

                    DROP TABLE IF EXISTS flour.dim_business CASCADE;
                    DROP TABLE IF  EXISTS flour.dim_rider CASCADE;
                    DROP TABLE IF  EXISTS flour.flour_type CASCADE;
                    DROP TABLE IF  EXISTS flour.orders_fact CASCADE;


                    CREATE TABLE IF NOT EXISTS flour.dim_business (
                    business_id VARCHAR  PRIMARY KEY,
                    business_name VARCHAR NOT NULL,
                    business_type VARCHAR ,
                    business_address VARCHAR,
                    contact_name VARCHAR NOT NULL, 
                    contact_phone VARCHAR NOT NULL
                    );



                    CREATE TABLE IF  NOT EXISTS flour.dim_rider (
                    rider_id  INT PRIMARY KEY,
                    rider_name VARCHAR NOT NULL, 
                    rider_phone VARCHAR NOT NULL);
                    

                    CREATE TABLE IF NOT EXISTS flour.dim_flour_type (
                    flour_id INT PRIMARY KEY,
                    flour_type VARCHAR
                    );

                    CREATE TABLE IF NOT EXISTS flour.orders_fact (
                    order_id VARCHAR PRIMARY KEY,
                    business_id VARCHAR NOT NULL REFERENCES flour.dim_business (business_id),
                    rider_id INT NOT NULL REFERENCES flour.dim_rider (rider_id), 
                    flour_id INT NOT NULL  REFERENCES flour.dim_flour_type (flour_id),
                    order_date  DATE NOT NULL,
                    total_amount FLOAT NOT NULL,
                    quantity_bags INT NOT NULL, 
                    price_per_bag FLOAT NOT NULL,
                    payment_method VARCHAR NOT NULL,
                    order_status VARCHAR NOT NULL
                    
                    );

'''
    cursor.execute(table_query)
    conn.commit()
    cursor.close()
    conn.close()
    print('Tables created sucessfully')

create_tables()

engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

dim_business.to_sql('dim_business', engine, schema = "flour", if_exists = 'append', index = False)
dim_rider.to_sql('dim_rider', engine, schema = "flour", if_exists = 'append', index = False)
dim_flour_type.to_sql('dim_flour_type', engine, schema = "flour", if_exists = 'append', index = False)
orders_fact.to_sql('orders_fact', engine, schema = "flour", if_exists = 'append', index = False)
print ('Data loaded to db sucessfully')