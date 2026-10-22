from dash import html
import dash_bootstrap_components as dbc 

def format_number(num, is_currency=False, is_percentage=False):
    
    if num is None:
        return "0"
    if is_currency:
        return f"${num:,.0f}"
    if is_percentage:
        return f"{num:.1f}%"
    if isinstance(num, float):
        return f"{num:,.1f}"
    return f"{num:,}"


def create_chart_card(title, chart_component):
    
    return dbc.Card(
        dbc.CardBody([
            html.H5(
                title,
                className="chart-card-title"
            ),
            html.Div(chart_component, className="chart-card-container")
        ]),
        className="chart-card"
    )

def normalize_fig(fig):
    fig.update_layout(
        template="plotly_dark",
        autosize=True,
        height=None,
        margin=dict(l=20,r=20,t=20,b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white", family="-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Vazirmatn', 'Vazir', 'IRANSans', 'Tahoma', sans-serif")
    )

    return fig