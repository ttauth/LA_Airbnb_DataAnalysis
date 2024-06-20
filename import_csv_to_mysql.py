import pandas as pd
import glob
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()


username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')


engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}")


for file in glob.glob("*.csv"):
    df = pd.read_csv(file)

    table_name = file.split('.')[0]  
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f'Table {table_name} has been created in the database.')

print('All CSV files have been imported into the database.')
