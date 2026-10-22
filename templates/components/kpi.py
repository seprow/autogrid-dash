from dash import html
import dash_bootstrap_components as dbc


def create_kpi_card(title, value, change):
    
    is_positive = "▲" in change or (change and change[0] not in ["-", "▼"])
    change_color = "#22c55e" if is_positive else "#ef4444"
    
    return dbc.Card(
        dbc.CardBody([
            html.H6(
                title,
                className="kpi-card-title"
            ),
            html.H2(
                value,
                className="kpi-card-value"
            ),
            html.P(
                change,
                className="kpi-card-change",
                style={"color": change_color}
            ),
        ]),
        className="kpi-card"
    )


def create_kpi_row(data=None):

    return html.Div(
        [
            html.Div(
                create_kpi_card(
                    item["title"], 
                    item["value"], 
                    item["change"], 
                ),
                className="kpi-item-wrapper"
            )
            for item in data
        ],
        className="kpi-row"
    )
