import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import yfinance as yf


dataF = yf.download("AAPL", start="2022-01-01", end="2022-12-31")


candlestick = go.Candlestick(x=dataF.index,
                             open=dataF['Open'],
                             high=dataF['High'],
                             low=dataF['Low'],
                             close=dataF['Close'])


layout = go.Layout(title='Японские свечи', xaxis=dict(rangeslider=dict(visible=False)))


fig = go.Figure(data=[candlestick], layout=layout)


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='График японских свечей'),
    dcc.Graph(
        id='candlestick-chart',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
