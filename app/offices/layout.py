import dash_html_components as html
import dash_core_components as dcc
import filters

content = [
    html.Div([
        html.H2('Offices', className='text-5xl'),
        filters.content,
        html.Div(
            className='flex flex-col',
            children=[
                dcc.Graph(
                    id='offices-sales',
                    figure={
                        'data': []
                    },
                ),
                dcc.Graph(
                    id='offices-revenue',
                    figure={
                        'data': []
                    },
                ),
            ],
        ),
    ]),
]
