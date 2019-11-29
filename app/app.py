import dash
import pandas as pd
from dash.dependencies import Output, Input, State
import dash_html_components as html
import offices.layout
import brands.layout
import products.layout
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:n0import4@localhost:5432/final-project')
sales_df = pd.read_sql('SELECT * FROM sales', engine.connect(), parse_dates=['date'])
sales_df['month_year'] = sales_df['date'].apply(lambda x: x.strftime("%Y-%m"))

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/uditagarwal/pen/oNvwKNP.css'])
app.config.suppress_callback_exceptions = True


def runQuery(sql):
    result = engine.connect().execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())


def filter_df(df, start_date, end_date):
    mask1 = df.date > start_date
    mask2 = df.date < end_date
    return df[mask1 & mask2]


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-offices':
        return offices.layout.office_layer
    elif tab == 'tab-2-brands':
        return brands.layout.brand_layer
    elif tab == 'tab-3-products':
        return products.layout.product_layer
