import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import repository
from filters import filters_data
from app import app
import pandas as pd


office_names = pd.DataFrame(filters_data['offices'], columns=['name'])


def get_offices_sales_chart(filters):
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
            'barmode': 'stack',
            'title': 'Sales through time'
        }
    }


def get_offices_revenue_chart(filters):
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
            'barmode': 'stack',
            'title': 'Revenue through time'
        }
    }


def update_filters_options(filters):
    distributors_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': filters['start_date'],
            'end_date': filters['end_date'],
            'categories': filters['categories'],
            'brands': filters['brands'],
            'offices': filters['offices']
        }).distributor.unique()
    ]

    brands_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': filters['start_date'],
            'end_date': filters['end_date'],
            'categories': filters['categories'],
            'distributors': filters['distributors'],
            'offices': filters['offices']
        }).brand.unique()
    ]

    categories_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': filters['start_date'],
            'end_date': filters['end_date'],
            'distributors': filters['distributors'],
            'brands': filters['brands'],
            'offices': filters['offices']
        }).category.unique()
    ]

    offices_options = [
        {'label': option, 'value': option}
        for option in repository.get_sales({
            'start_date': filters['start_date'],
            'end_date': filters['end_date'],
            'categories': filters['categories'],
            'distributors': filters['distributors'],
            'brands': filters['brands']
        }).office.unique()
    ]
    return [distributors_options, brands_options, categories_options, offices_options]


def update_indicators(filters):
    dff = repository.get_sales(filters)
    sells = dff['office'].value_counts()
    revenue = dff.groupby('office').sale_amount.sum()

    top_distributors = dff['distributor'].value_counts().sort_values().index[:5]
    top_distributors_list = [html.Li(dist) for dist in top_distributors]

    top_products = dff['brand'].value_counts().sort_values().index[:5]
    top_products_list = [html.Li(prod) for prod in top_products]

    return [f"{sells.idxmax()}: {sells.max()}",
            f"{revenue.idxmax()}: {revenue.max()} COP",
            top_distributors_list,
            top_products_list]


@app.callback(
    [
        Output('offices-sales', 'figure'),
        Output('offices-revenue', 'figure'),
        Output('distributors-filter', 'options'),
        Output('brands-filter', 'options'),
        Output('categories-filter', 'options'),
        Output('offices-filter', 'options'),
        Output('top-office-sells', 'children'),
        Output('top-office-revenue', 'children'),
        Output('top-distributors', 'children'),
        Output('top-products', 'children'),
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
    filters = {
        'start_date': start_date,
        'end_date': end_date,
        'distributors': distributors,
        'categories': categories,
        'brands': brands,
        'offices': offices
    }
    return [
        get_offices_sales_chart(filters),
        get_offices_revenue_chart(filters),
    ] + update_filters_options(filters) + update_indicators(filters)
