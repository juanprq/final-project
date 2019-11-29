import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt

content = html.Div(
    className='rounded shadow-lg p-4 bg-gray-100 flex flex-wrap',
    children=[
        html.Div(
            className='w-full p-4 flex flex-col',
            children=[
                html.Div(children='Date Range:'),
                dcc.DatePickerRange(
                    id='date-range-filter',
                    min_date_allowed=dt(1995, 8, 5),
                    max_date_allowed=dt(2017, 9, 19),
                    initial_visible_month=dt(2017, 8, 5),
                    end_date=dt(2017, 8, 25)
                ),
            ],
        ),
        html.Div(
            className='w-1/2 p-4 flex flex-col',
            children=[
                html.Div(children='Distributors:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'NYC'],
                    multi=True
                ),
            ],
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Brands:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'NYC'],
                    multi=True
                ),
            ]
        ),
        html.Div(

            className='w-1/2 p-4',
            children=[
                html.Div(children='Categories:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'NYC'],
                    multi=True
                ),
            ]
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Offices:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montreal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value=['MTL', 'NYC'],
                    multi=True
                ),
            ]
        ),
    ],
)
