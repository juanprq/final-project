import repository
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
import numpy as np

filters_data = repository.get_initial_filter()

content = html.Div(
    className='rounded shadow-lg p-4 bg-gray-100 flex flex-wrap',
    children=[
        html.Div(
            className='w-full p-4 flex flex-col',
            children=[
                html.Div(children='Date Range:'),
                dcc.DatePickerRange(
                    id='date-range-filter',
                    min_date_allowed=filters_data['start_date'],
                    max_date_allowed=filters_data['end_date'],
                    start_date=filters_data['start_date'],
                    end_date=filters_data['end_date'],
                ),
            ],
        ),
        html.Div(
            className='w-1/2 p-4 flex flex-col',
            children=[
                html.Div(children='Distributors:'),
                dcc.Dropdown(
                    id='distributors-filter',
                    options=[],
                    multi=True,
                    # value=['Grandes Superficies']
                    value=[]

                ),
            ],
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Brands:'),
                dcc.Dropdown(
                    id='brands-filter',
                    options=[],
                    multi=True,
                    # value=['Criollas']
                    value=[]

                ),
            ]
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Categories:'),
                dcc.Dropdown(
                    id='categories-filter',
                    options=[],
                    multi=True,
                    # value=['Producto En Frituras']
                    value=[]

                ),
            ]
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Offices:'),
                dcc.Dropdown(
                    id='offices-filter',
                    options=[],
                    multi=True,
                    # value=['Cali']
                    value=[]
                ),
            ]
        ),
    ],
)
