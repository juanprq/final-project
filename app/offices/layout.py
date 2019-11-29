import dash_html_components as html
import filters

content = [
    html.Div([
        html.H2('Offices', className='text-5xl'),
        filters.content,
    ]),
]
