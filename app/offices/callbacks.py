import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from app import app

# ---------
# -- TODO: We need to add the query to the db in order to build the charts corretly
# ---------

def get_offices_sales_chart():
    return {
        'data': [
            go.Bar(
                name=office_names.loc[idx, 'name'],
                x=dates,
                y=sells[idx].sort_index().values
            ) for idx in sorted(office_ids)
        ],
        'layout': {
            'barmode': 'stack'
        }
    }

def get_offices_revenue_chart():
    return {
        'data': [
            go.Bar(
                name=office_names.loc[idx, 'name'],
                x=dates,
                y=revenue[idx].sort_index().values
            ) for idx in sorted(office_ids)
        ],
        'layout': {
            'barmode': 'stack'
        }
    }

@app.callback(
    [
        Output('offices-sales', 'children'),
        Output('offices-revenue', 'children'),
    ],
    [
        Input('date-range-filter', 'start_date'),
        Input('date-range-filter', 'end_date'),
        Input('distributors-filter', 'value'),
        Input('brands-filter', 'value'),
        Input('categories-filter', 'value'),
        Input('offices-filter', 'value'),
    ])
def display_value(start_date, end_date, distributors, brands, categories, offices):
    return [
        get_offices_sales_chart(),
        get_offices_revenue_chart(),
    ]
