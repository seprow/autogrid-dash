from abc import ABC, abstractmethod
import importlib
import inspect
from pathlib import Path
from dash import html

class Page(ABC):
    
    def __init__(self, config):
        self.config = config
    
    @abstractmethod
    def render(self):
        pass
    
    def get_container(self):
        return html.Div(
            self.render(), 
            className="page-content"
        )


class DefaultPage(Page):
 
    def render(self):
        return html.Div([
            html.H3("Welcome to Dashboard", className="default-page"),
            html.P("Select a menu item from sidebar", className="default-page"),
        ], className="page-content")


class PageRegistry:
    
    def __init__(self, config):
        self.config = config
        self.pages = {}
        self._load_pages()
    
    def _load_pages(self):

        pages_dir = Path(__file__).parent.parent.parent / "pages"
        
        if pages_dir.exists():
            for page_file in pages_dir.glob("*_page.py"):
                module_name = f"pages.{page_file.stem}"
                try:
                    module = importlib.import_module(module_name)
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and issubclass(obj, Page) 
                            and obj != Page and obj != DefaultPage):
                            page_id = page_file.stem.replace("_page", "")
                            self.pages[page_id] = obj
                except Exception as e:
                    print(f"Error loading page {page_file}: {e}")
        
    
    def register_page(self, page_id, page_class):
        if issubclass(page_class, Page):
            self.pages[page_id] = page_class
    
    def get_page(self, page_id):
        page_class = self.pages.get(page_id)
        if page_class:
            return page_class(self.config)
        return DefaultPage(self.config)
    
    def get_all_page_ids(self):
        return list(self.pages.keys())
    

