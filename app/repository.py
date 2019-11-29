import sqlalchemy as db

engine = db.create_engine('postgresql://user:password@localhost:5432/final_project')
connection = engine.connect()

def fetchQueryResult(query):
    resultProxy = connection.execute(query)
    return resultProxy.fetchall()

#GET ALL POSSIBLE VALUES FOR THE FILTERS
def get_filter_values():
    filters = {
        'start_date': fetchQueryResult('SELECT MIN(date) FROM sales')[0][0],
        'end_date': fetchQueryResult('SELECT MAX(date) FROM sales')[0][0],
        'offices': fetchQueryResult('SELECT * FROM locations'),
        'distributors': fetchQueryResult('SELECT * FROM distributors'),
        'categories': fetchQueryResult('SELECT DISTINCT category FROM products')
    }
    return filters
#GET NUMBER OF SALES BETWEEN FILTERS
def get_number_sales(filters):
    
    print('')

print(get_filter_values())
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


    