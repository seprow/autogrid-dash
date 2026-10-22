from dash import Dash, html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

from config import DashboardConfig
from templates.components import (
    create_sidebar, 
    create_kpi_row,
    create_footer,
)
from templates.pages import Page, PageRegistry, DefaultPage
from pages.kpi import kpi_data


class DashboardTemplate:
    
    def __init__(self, config=None, kpi=None):
        self.config = config if config else DashboardConfig()
        self.app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.kpi_data = kpi
        self.page_registry = PageRegistry(self.config)
        self._register_pages_from_config()
        self._setup_layout()
        self._setup_callbacks()
    
    def _register_pages_from_config(self):
  
        if hasattr(self.config, 'SIDEBAR_ITEMS'):
            for item in self.config.SIDEBAR_ITEMS:
                page_id = item['id']
              
                if page_id not in self.page_registry.pages:

                    page_class = self._create_dynamic_page_class(page_id, item['name'])
                    self.page_registry.register_page(page_id, page_class)
    
    def _create_dynamic_page_class(self, page_id, page_name):
        
        class DynamicPage(Page):
            def render(self):
                return html.Div([
                    html.H3(page_name, 
                            className="default-page"), 
                    html.P(f"Content for {page_name} page will be displayed here.",
                          className="default-page")
                ])
        
        return DynamicPage
    
    def _setup_layout(self):

        sidebar = create_sidebar(self.config)
        kpi_row = create_kpi_row(self.kpi_data)
        footer = create_footer(self.config)
        
        main_content = html.Div([
            kpi_row,
            html.Div(id="dashboard-content", className="page-content"),
            footer
        ], className="main-content")
        
        self.app.layout = html.Div(
            [sidebar, main_content],
            className="layout"
        )
    

    def _setup_callbacks(self):

        @self.app.callback(
            Output("dashboard-content", "children"),
            [Input(f"sidebar-item-{item['id']}", "n_clicks") 
             for item in self.config.SIDEBAR_ITEMS]
        )
        def update_content(*args):
            ctx = callback_context
            if not ctx.triggered:
                return self.get_default_content()
            
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            item_id = button_id.replace("sidebar-item-", "")
            
            return self.get_page_content(item_id)
    
    def get_default_content(self):
        default_page = DefaultPage(self.config)
        return default_page.get_container()
    
    def get_page_content(self, page_id):
        page = self.page_registry.get_page(page_id)
        return page.get_container()
    
    def register_custom_page(self, page_id, page_class):
        self.page_registry.register_page(page_id, page_class)
    
    def run(self, debug=True, port=8050):
        self.app.run(debug=debug, port=port)



if __name__ == "__main__":

    dashboard = DashboardTemplate(kpi=kpi_data())
    
    #print(dashboard.page_registry.get_all_page_ids())
    #dashboard.register_custom_page("revenue", CustomRevenuePage)
    
    dashboard.run()





