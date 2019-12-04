import dash_core_components as dcc
import dash_html_components as html
from app import app
from offices import callbacks

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H1(children='SnaCo Sales Dashboard', className='text-6xl'),
        ],
        className='study-browser-banner row'
    ),
    html.Div(className='container mx-auto', children=[
        dcc.Tabs(id='tabs', value='offices-tab', children=[
            dcc.Tab(label='Offices', value='offices-tab'),
            dcc.Tab(label='Brands', value='brands-tab'),
            dcc.Tab(label='Products', value='products-tab'),
        ]),
        html.Div(id='tab-content', className='py-4'),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
