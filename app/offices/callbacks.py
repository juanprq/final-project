import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import repository
from filters import filters_data
from app import app
import pandas as pd

# ---------
# -- TODO: We need to add the query to the db in order to build the charts corretly
# ---------

office_names = pd.DataFrame(filters_data['offices'], columns=['id', 'name'])


def get_offices_sales_chart(start_date, end_date):
    dff = repository.filter_df(repository.sales, start_date, end_date)
    dates = dff.month_year.sort_values().unique()
    office_ids = dff.office_id.unique()
    sells = dff.groupby('office_id').month_year.value_counts()

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


def get_offices_revenue_chart(start_date, end_date):
    dff = repository.filter_df(repository.sales, start_date, end_date)
    dates = dff.month_year.sort_values().unique()
    office_ids = dff.office_id.unique()
    revenue = dff.groupby(['office_id', 'month_year']).sale_amount.sum()

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
        Output('offices-sales', 'figure'),
        Output('offices-revenue', 'figure'),
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
        get_offices_sales_chart(start_date, end_date),
        get_offices_revenue_chart(start_date, end_date),
    ]
