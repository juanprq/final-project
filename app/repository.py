import os
import sqlalchemy as db

from dotenv import load_dotenv
load_dotenv()

host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

engine = db.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
connection = engine.connect()

def fetch_query_results(query):
    resultProxy = connection.execute(query)
    return resultProxy.fetchall()

#GET ALL POSSIBLE VALUES FOR THE FILTERS
def get_filter_values():
    filters = {
        'start_date': fetch_query_results('SELECT MIN(date) FROM sales')[0][0],
        'end_date': fetch_query_results('SELECT MAX(date) FROM sales')[0][0],
        'offices': fetch_query_results('SELECT * FROM locations'),
        'distributors': fetch_query_results('SELECT * FROM distributors'),
        'categories': fetch_query_results('SELECT DISTINCT category FROM products')
    }
    return filters
#GET NUMBER OF SALES BETWEEN FILTERS
def get_number_sales(filters):
    print('')

#FILTER MODEL
#filters = {
#    start_date: 'date',
#    end_date: 'date',
#    offices: [
#        (id1, 'office1'),
#        (id2, 'office2')
#    ],
#    distributors: [
#        (id1, 'distributor1'),
#        (id2, 'distributor2')
#    ],
#    categories: ['category1','category2'],
#};

