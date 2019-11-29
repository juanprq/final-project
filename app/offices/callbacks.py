from app import app, sales_df, runQuery, filter_df
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import numpy as np
import pandas as pd


office_names = runQuery('''
    SELECT DISTINCT name from locations
    JOIN sales ON sales.office_id = locations.id
''')


@app.callback(
    Output('offices-sales', 'figure'),
    [
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
    ]
)
def update_office_sales(start_date, end_date):
    dff = filter_df(sales_df, start_date, end_date)
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


@app.callback(
    Output('offices-revenue', 'figure'),
    [
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date')
    ]
)
def update_office_revenue(start_date, end_date):
    dff = filter_df(sales_df, start_date, end_date)
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
