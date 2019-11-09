import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import offices
import brands
import products
from dash.dependencies import Output, Input, State

token = 'pk.eyJ1IjoibmV3dXNlcmZvcmV2ZXIiLCJhIjoiY2o2M3d1dTZiMGZobzMzbnp2Z2NiN3lmdyJ9.cQFKe3F3ovbfxTsM9E0ZSQ'
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/uditagarwal/pen/oNvwKNP.css'])

dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y')
snacks_df = pd.read_csv('./clean_snacks.csv', dtype={ 'client_id': str }, parse_dates=['date'], date_parser=dateparse)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H2(children="SnaCo Sales Dashboard", className='h2-title'),
            html.Div(
                className='div-logo padding-top-bot',
                children=[
                    dcc.DatePickerRange(
                    id='date-picker-range', # The id of the DatePicker, its always very important to set an Id for all our components
                    start_date=snacks_df['date'].min(), # The start_date is going to be the min of Order Date in our dataset
                    end_date=snacks_df['date'].max(),
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
    html.Div(id='tabs-content-example'),])

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-offices':
        return offices.office_layer
    elif tab == 'tab-2-brands':
        return brands.brand_layer
    elif tab == 'tab-3-products':
        return products.product_layer
if __name__ == "__main__":
    app.run_server(debug=True)