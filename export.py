
import pandas as pd
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
RAW_DATA_DIR = PROJECT_ROOT / "raw_dataset"
CLEANED_DATA_DIR = PROJECT_ROOT / "cleaned_dataset"

df = pd.read_csv(r'C:\Users\Admin\Desktop\10Alytics\flour4four_etl_with_airflow\raw_dataset\flour4four_orders_oct2025.csv')
print('data extracted sucessfully')

df['order_date'] = df['order_date'].fillna(df['delivery_date'])
df['order_date'] = pd.to_datetime(df['order_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
df['rider_phone'] = df['rider_phone'].astype(str)
df['total_amount'] = df['total_amount'].astype(float)
df['contact_phone'] = df['contact_phone'].astype(str)
print ('Data types handled')

df['business_name'] = df['business_name'].fillna('Unknown')
df['business_type'] = df['business_type'].fillna('Unknown')
df['business_address'] = df['business_address'].fillna('Unknown')
df['flour_type'] = df['flour_type'].fillna('Unknown')
df['price_per_bag'] = df['price_per_bag'].fillna(df['price_per_bag'].median())

print ('Missing values handled')

df.to_csv(CLEANED_DATA_DIR/'flour4four_cleaned_orders_data.csv', index = False)
print ('cleaned csv file created')
