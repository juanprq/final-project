import dash
from dash.dependencies import Output, Input, State
import dash_html_components as html
import offices.layout
import brands.layout
import products.layout

app = dash.Dash(__name__, external_stylesheets=[
    'https://codepen.io/uditagarwal/pen/oNvwKNP.css',
    'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.1.2/base.css',
    'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.1.2/components.css',
    'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.1.2/tailwind.css',
    'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.1.2/utilities.css',
])
app.config.suppress_callback_exceptions = True

@app.callback(Output('tab-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'offices-tab':
        return offices.layout.content
    elif tab == 'brands-tab':
        return brands.layout.content
    elif tab == 'products-tab':
        return products.layout.content
