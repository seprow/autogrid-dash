from abc import ABC
from dash import html, dash_table, dcc
import dash_bootstrap_components as dbc
import pandas as pd
from templates.pages import Page
import dash
from dash import dash_table, html, dcc
import pandas as pd
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

family = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Vazirmatn', 'Vazir', 'IRANSans', 'Tahoma', sans-serif"

table = html.Div(
    style={
        'background': '#071426',
        'minHeight': '100vh',
        'padding': '40px',
        'fontFamily': family
    },
    children=[
        html.H1(
            '',
            style={'color': '#38bdf8', 'textAlign': 'center', 'marginBottom': '30px'}
        ),
        
        dash_table.DataTable(
            id='glass-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            
            style_table={
                'overflowX': 'auto',
                'borderRadius': '16px',
                'backdropFilter': 'blur(12px)',
                'background': 'rgba(15, 23, 42, 0.5)',
                'border': '1px solid rgba(56, 189, 248, 0.2)'
            },
            
            style_header={
                'backgroundColor': 'rgba(56, 189, 248, 0.15)',
                'color': '#38bdf8',
                'fontWeight': 'bold',
                'textAlign': 'center',
                'border': '1px solid rgba(56, 189, 248, 0.2)',
                'fontFamily': family,
                'fontSize': '14px'
            },
            
            style_cell={
                'textAlign': 'center',
                'backgroundColor': 'rgba(30, 41, 59, 0.4)',
                'color': '#e2e8f0',
                'border': '1px solid rgba(255, 255, 255, 0.05)',
                'padding': '12px',
                'fontFamily': family,
                'fontSize': '12px'
            },
            
            style_data_conditional=[
                {'if': {'row_index': 'odd'}, 'backgroundColor': 'rgba(255, 255, 255, 0.02)'},
                {'if': {'column_id': 'lifeExp'}, 'color': '#4ade80'},
                {'if': {'column_id': 'gdpPercap'}, 'color': '#fbbf24'}
            ],
            
            sort_action='native',
            filter_action='native',
            page_size=10,
            page_action='native',
            
            style_cell_conditional=[{
                'if': {'column_id': 'country'},
                'textAlign': 'left'
            }]
        )
    ]
)

class Table(Page):
    def render(self):
        return table