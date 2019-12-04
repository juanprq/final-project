import dash_html_components as html
import dash_core_components as dcc
import filters

content = html.Div([
    html.H2('Brands', className='text-5xl'),
    filters.content,
])
