import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import repository
from filters import filters_data
from app import app
import pandas as pd


office_names = pd.DataFrame(filters_data['offices'], columns=['name'])


def get_offices_sales_chart(start_date, end_date, distributors, brands, categories, offices):
    filters = {
        'start_date': start_date,
        'end_date': end_date,
        'distributors': distributors,
        'categories': categories,
        'brands': brands,
        'offices': offices
    }
    dff = repository.get_sales(filters)
    dff['month_year'] = dff['date'].apply(lambda x: x.strftime('%Y-%m'))
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


def get_offices_revenue_chart(start_date, end_date, distributors, brands, categories, offices):
    filters = {
        'start_date': start_date,
        'end_date': end_date,
        'distributors': distributors,
        'categories': categories,
        'brands': brands,
        'offices': offices
    }
    dff = repository.get_sales(filters)
    dff['month_year'] = dff['date'].apply(lambda x: x.strftime('%Y-%m'))
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


def update_filters_options(start_date, end_date, distributors, brands, categories, offices):
    distributors_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': start_date,
            'end_date': end_date,
            'categories': categories,
            'brands': brands,
            'offices': offices
        }).distributor.unique()
    ]

    brands_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': start_date,
            'end_date': end_date,
            'categories': categories,
            'distributors': distributors,
            'offices': offices
        }).brand.unique()
    ]

    categories_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': start_date,
            'end_date': end_date,
            'distributors': distributors,
            'brands': brands,
            'offices': offices
        }).category.unique()
    ]

    offices_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': start_date,
            'end_date': end_date,
            'categories': categories,
            'distributors': distributors,
            'brands': brands
        }).office.unique()
    ]
    return [distributors_options, brands_options, categories_options, offices_options]


@app.callback(
    [
        Output('offices-sales', 'figure'),
        Output('offices-revenue', 'figure'),
        Output('distributors-filter', 'options'),
        Output('brands-filter', 'options'),
        Output('categories-filter', 'options'),
        Output('offices-filter', 'options'),
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
        get_offices_sales_chart(start_date, end_date, distributors, brands, categories, offices),
        get_offices_revenue_chart(start_date, end_date, distributors, brands, categories, offices),
    ] + update_filters_options(start_date, end_date, distributors, brands, categories, offices)
