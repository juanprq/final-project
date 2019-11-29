import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Output, Input, State
import offices.callbacks
import brands.callbacks
import products.callbacks
from app import app, sales_df

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H2(children="SnaCo Sales Dashboard", className='h2-title'),
            html.Div(
                className='div-logo padding-top-bot',
                children=[
                    dcc.DatePickerRange(
                        id='date-picker-range',  # The id of the DatePicker, its always very important to set an Id for all our components
                        start_date=sales_df['date'].min(),  # The start_date is going to be the min of Order Date in our dataset
                        end_date=sales_df['date'].max(),
                    )
                ]
            )
        ],
        className='study-browser-banner row'
    ),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Offices', value='tab-1-offices'),
        dcc.Tab(label='Brands', value='tab-2-brands'),
        dcc.Tab(label='Products', value='tab-3-products'),
    ]),
    html.Div(id='tabs-content-example'), ])


if __name__ == "__main__":
    app.run_server(debug=True)