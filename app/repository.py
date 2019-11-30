import pandas as pd
import sqlalchemy as db
import datetime

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
#    brands: [
#        ('brand1',''),
#        ('brand1','')
#    ]
#};

engine = db.create_engine('postgresql://postgres:hipocampos97@localhost:5432/final_project')
connection = engine.connect()

def fetchQueryResult(query):
    resultProxy = connection.execute(query)
    return resultProxy.fetchall()

#GET ALL POSSIBLE VALUES FOR THE FILTERS
def get_filter_values():
    filters = {
        'start_date': fetchQueryResult('SELECT MIN(date) FROM sales')[0][0],
        'end_date': fetchQueryResult('SELECT MAX(date) FROM sales')[0][0],
        'offices': fetchQueryResult('SELECT id,name FROM locations'),
        'distributors': fetchQueryResult('SELECT id,name FROM distributors'),
        'categories': fetchQueryResult('SELECT DISTINCT category FROM products',
        'brands': fetchQueryResult('SELECT DISTINCT brand FROM products'))
    }
    return filters

#GET NUMBER OF SALES BETWEEN FILTERS
def get_sales(filters):
    sales = pd.read_sql(('select * from "sales" where'
                        '"date" BETWEEN %(start_date)s AND %(end_date)s AND'
                        '""'),
                       connection,params={'start_date':filters['start_date'],'end_date':filters['end_date']})
    return(sales)



print(get_sales(get_filter_values()))
    