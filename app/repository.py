import pandas as pd
import os
import sqlalchemy as db
import datetime

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
        'offices': fetch_query_results('SELECT id,name FROM locations'),
        'distributors': fetch_query_results('SELECT id,name FROM distributors'),
        'categories': fetch_query_results('SELECT DISTINCT category FROM products'),
        'brands': fetch_query_results('SELECT DISTINCT brand FROM products')
    }
    return filters

#STRINGIFY FILTERS TO WHEN CLAUSE
def stringify_filter(filters):
    where = ''
    if len(filters['offices']) > 0:
        offices = ''
        for i in filters['offices']:
            offices = f"{offices}'{i[1]}',"
        where = f'AND l.name in ({offices[:-1]})'
    if len(filters['distributors']) > 0:
        distributors = ''
        for i in filters['distributors']:
            distributors = f"{distributors}'{i[1]}',"
        where = f'{where} AND d.name in ({distributors[:-1]})'
    if len(filters['categories']) > 0:
        categories = ''
        for i in filters['categories']:
            categories = f"{categories}'{i[0]}',"
        where = f'{where} AND p.category in ({categories[:-1]})'
    if len(filters['brands']) > 0:
        brands = ''
        for i in filters['brands']:
            brands = f"{brands}'{i[0]}',"
        where = f'{where} AND p.brand in ({brands[:-1]})'
    return where
        
#GET SALES WITH FILTERS
def get_sales(filters):
    where_clause = stringify_filter(filters)
    sales = pd.read_sql(("select p.id as product_id,s.flavor,s.date,s.units,s.devolution_units,s.sale_amount,"
                         "s.sale_discount,s.sale_devolution,s.incentive,l.name as office, lw.name as warehouse,"
                         "d.name as distributor, ls.name as point_of_sale from sales as s "
                         "JOIN locations as l on l.id = s.office_id "
                         "JOIN locations as lw on lw.id = s.warehouse_id "
                         "JOIN locations as ls on ls.id = s.point_of_sale_id "
                         "JOIN distributors as d on d.id = s.distributor_id "
                         "JOIN products as p on p.id = s.product_id "
                         "WHERE s.date BETWEEN %(start_date)s AND %(end_date)s "
                         f"{where_clause}"
                        ),
                       connection,params={'start_date':filters['start_date'],'end_date':filters['end_date']})
    return(sales)
