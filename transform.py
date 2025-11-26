import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
RAW_DATA_DIR = PROJECT_ROOT / "raw_dataset"#
CLEANED_DATA_DIR = PROJECT_ROOT / "cleaned_dataset"


df = pd.read_csv(CLEANED_DATA_DIR/'flour4four_cleaned_orders_data.csv')
print ('cleaned data loaded successfully')

dim_business = df[['business_id','business_name','business_type','business_address', 'contact_name', 'contact_phone']].copy().drop_duplicates(subset ='business_id').reset_index(drop =True)
dim_business.head()

dim_rider = df[['rider_name', 'rider_phone']].copy().drop_duplicates().reset_index(drop = True)
dim_rider['rider_id']= dim_rider.index +1
dim_rider = dim_rider[['rider_id','rider_name', 'rider_phone']]
dim_rider.head()

dim_flour_type = df[['flour_type']].copy().drop_duplicates().reset_index(drop = True)
dim_flour_type['flour_id'] = range(1, len(dim_flour_type)+1 )
dim_flour_type = dim_flour_type[['flour_id','flour_type']]
dim_flour_type.head()

orders_fact = df.copy()

orders_fact = orders_fact.merge(dim_rider, on =['rider_name', 'rider_phone'], how ='left')\
                       .merge(dim_flour_type, on = 'flour_type', how ='left')\
                        [['order_id','business_id','rider_id', 'flour_id','order_date','total_amount','quantity_bags', 'price_per_bag','payment_method','order_status']]
orders_fact.head()

dim_rider.to_csv(r'C:\Users\Admin\Desktop\10Alytics\flour4four_etl_with_airflow\cleaned_dataset\dim_rider.csv')
dim_business.to_csv(r'C:\Users\Admin\Desktop\10Alytics\flour4four_etl_with_airflow\cleaned_dataset\dim_business.csv')
dim_flour_type.to_csv(r'C:\Users\Admin\Desktop\10Alytics\flour4four_etl_with_airflow\cleaned_dataset\dim_flour_type.csv')
orders_fact.to_csv(r'C:\Users\Admin\Desktop\10Alytics\flour4four_etl_with_airflow\cleaned_dataset\orders_fact.csv')
print ('dfs exported to csv successfully')