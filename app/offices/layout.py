import dash_html_components as html
import dash_core_components as dcc

office_layer = html.Div([
    html.H3('Offices'),
    html.Div(
        className='twelve columns card',
        children=[
            dcc.Graph(
                id='offices-sales',
                figure={
                    'data': []
                }
            )
        ]
    ),
    html.Div(
        className='twelve columns card',
        children=[
            dcc.Graph(
                id='offices-revenue',
                figure={
                    'data': []
                }
            )
        ]
    )
])
