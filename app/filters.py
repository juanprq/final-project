import repository
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
filters_data = repository.get_filter_values()

def build_option_list(options):
    return [{ 'label': option[1], 'value': option[0] } for option in options]

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
                    options=build_option_list(filters_data['distributors']),
                    multi=True
                ),
            ],
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Brands:'),
                dcc.Dropdown(
                    id='brands-filter',
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
                    id='categories-filter',
                    options=[{'label': cat[0], 'value': cat[0]} for cat in filters_data['categories']],
                    multi=True
                ),
            ]
        ),
        html.Div(
            className='w-1/2 p-4',
            children=[
                html.Div(children='Offices:'),
                dcc.Dropdown(
                    id='offices-filter',
                    options=build_option_list(filters_data['offices']),
                    multi=True
                ),
            ]
        ),
    ],
)
