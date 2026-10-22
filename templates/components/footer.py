from dash import html
from datetime import datetime, timedelta

from config import DashboardConfig

def create_footer(config=None):
    
    if config is None:
        config = DashboardConfig
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    return html.Div([
        html.Hr(className="footer-hr"),
        html.Div(
            f"{config.FOOTER_TEXT}: {current_time}",
            className="footer-text"
        )
    ], className="footer")