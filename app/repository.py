import pandas as pd
import numpy as np
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

# GET ALL POSSIBLE VALUES FOR THE FILTERS


def get_initial_filter():
    filters = {
        'start_date': fetch_query_results('SELECT MIN(date) FROM sales')[0][0],
        'end_date': fetch_query_results('SELECT MAX(date) FROM sales')[0][0],
        'offices': fetch_query_results('SELECT name FROM locations'),
        'distributors': fetch_query_results('SELECT name FROM distributors'),
        'categories': fetch_query_results('SELECT DISTINCT category FROM products'),
        'brands': fetch_query_results('SELECT DISTINCT brand FROM products')
    }
    return filters


# STRINGIFY FILTERS TO WHEN CLAUSE


def stringify_filter(filters):
    where = ''
    if 'offices' in filters.keys() and len(filters['offices']) > 0:
        offices = ''
        for i in filters['offices']:
            if not isinstance(i, str):
                offices = f"{offices}'{i[0]}',"
            else:
                offices = f"{offices}'{i}',"
        where = f'AND l.name in ({offices[:-1]})'
    if 'distributors' in filters.keys() and len(filters['distributors']) > 0:
        distributors = ''
        for i in filters['distributors']:
            if not isinstance(i, str):
                distributors = f"{distributors}'{i[0]}',"
            else:
                distributors = f"{distributors}'{i}',"
        where = f'{where} AND d.name in ({distributors[:-1]})'
    if 'categories' in filters.keys() and len(filters['categories']) > 0:
        categories = ''
        for i in filters['categories']:
            if not isinstance(i, str):
                categories = f"{categories}'{i[0]}',"
            else:
                categories = f"{categories}'{i}',"
        where = f'{where} AND p.category in ({categories[:-1]})'
    if 'brands' in filters.keys() and len(filters['brands']) > 0:
        brands = ''
        for i in filters['brands']:
            if not isinstance(i, str):
                brands = f"{brands}'{i[0]}',"
            else:
                brands = f"{brands}'{i}',"
        where = f'{where} AND p.brand in ({brands[:-1]})'

    return where


# GET SALES WITH FILTERS
def get_sales(filters):
    where_clause = stringify_filter(filters)
    sales = pd.read_sql(("SELECT p.brand as brand, p.category, f.name as flavor, s.date,s.units,s.devolution_units,s.sale_amount,"
                         "s.sale_discount,s.sale_devolution,s.incentive,l.name as office, s.office_id,"
                         "lw.name as warehouse, ps.name as point_of_sale, d.name as distributor FROM sales as s "
                         "JOIN locations as l on l.id = s.office_id "
                         "JOIN locations as lw on lw.id = s.warehouse_id "
                         "LEFT JOIN points_of_sale as ps on ps.id = s.point_of_sale_id "
                         "JOIN distributors as d on d.id = s.distributor_id "
                         "JOIN products as p on p.id = s.product_id "
                         "JOIN flavors as f on f.id = s.flavor_id "
                         "WHERE s.date BETWEEN %(start_date)s AND %(end_date)s "
                         f"{where_clause}"
                         "LIMIT 100000"
                         ),
                        connection, params={'start_date': filters['start_date'], 'end_date': filters['end_date']})
    return sales
