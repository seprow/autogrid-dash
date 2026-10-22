from dash import html
from config import DashboardConfig


def create_sidebar(config=None):

    if config is None:
        config = DashboardConfig
    
    return html.Div(
        [
            html.Div(
                [
                    html.H2(
                        config.DASHBOARD_TITLE,
                        className="sidebar_title"
                    ),
                    html.P(
                        config.DASHBOARD_SUBTITLE,
                        className="sidebar_subtitle"
                    ),
                ]
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Span(item["name"], className="sidebar-item-name")
                        ],
                        className="sidebar-item",
                        id=f"sidebar-item-{item['id']}",
                        **{
                            "data-id": item["id"],
                            "data-name": item["name"]
                        }
                    ) for item in config.SIDEBAR_ITEMS
                ],
                className="sidebar-items-container"
            ),
            html.Div(
                [
                    html.Hr(className="sidebar-divider"),
                    html.Div(
                        "Version 1.0.0",
                        className="sidebar-footer-text"
                    ),
                    html.Div(
                        html.A(f"© 2026 Seprow", href="https://github.com/seprow"),
                        className="sidebar-footer-text"
                    )
                ],
                className="sidebar-footer"
            )
        ],

        className="sidebar"
    )