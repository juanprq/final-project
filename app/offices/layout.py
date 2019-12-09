import dash_html_components as html
import dash_core_components as dcc
import filters
import repository


content = [
    html.Div([
        html.H2('Offices', className='text-5xl'),
        filters.content,
        html.Div(
            className='flex flex-row w-full',
            children=[
                html.Div(
                    className='w-8/12',
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
                        html.Div(
                            className='w-4/12 indicator pretty_container text-teal-700 text-center bg-blue-100 px-4 py-10 m-2',
                            children=[
                                html.P('MOST SELLS OFFICE', className='twelve columns indicator_text font-sans text-4xl font-bold'),
                                html.P(id='top-office-sells', className='indicator_value text-3xl')
                            ]
                        ),
                        html.Div(
                            className='w-4/12 indicator pretty_container text-teal-700 text-center bg-blue-100 px-4 py-10 m-2',
                            children=[
                                html.P('MOST REVENUE OFFICE', className='twelve columns indicator_text font-sans text-4xl font-bold'),
                                html.P(id='top-office-revenue', className='indicator_value text-3xl')
                            ]
                        ),
                        html.Div(
                            className='w-4/12 indicator pretty_container text-teal-700 text-center bg-blue-100 px-4 py-10 m-2',
                            children=[
                                html.P('TOP DISTRIBUTORS', className='twelve columns indicator_text font-sans text-4xl font-bold'),
                                html.Ol(id='top-distributors', className='indicator_value text-3xl')
                            ]
                        ),
                        html.Div(
                            className='w-4/12 indicator pretty_container text-teal-700 text-center bg-blue-100 px-4 py-10 m-2',
                            children=[
                                html.P('TOP PRODUCTS', className='twelve columns indicator_text font-sans text-4xl font-bold'),
                                html.Ol(id='top-products', className='indicator_value text-3xl')
                            ]
                        )
                    ],
                ),
            ]),
    ])
]
