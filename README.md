# Interactive Dashboard Framework with AutoGrid

A framework for building interactive dashboards with **Plotly Dash**, featuring an automatic grid layout system.

## Goal

Leverage the flexibility and power of Python and Plotly for data analysis without having to deal with UI implementation and layout management.

**Note:** The charts and KPI values currently displayed are sample data. They are not connected to a live data source or database.

## Installation and Usage

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Dashboard Configuration

The main dashboard settings are defined in `config.py`.

Example sidebar menu configuration:

```python
SIDEBAR_ITEMS = [
    {"name": "Overview", "id": "overview"},
    {"name": "Table", "id": "table"},
]
```

Each `id` uniquely identifies a page and must be unique across the dashboard.

## Adding a New Page

Follow these steps to add a new page to the dashboard.

### 1. Create a Page Module

Create a new Python file inside the `pages/` directory. The filename must end with `_page.py`.

For example, `sales_page.py`.

### 2. Implement the Page Class

Define a class that inherits from `Page` and implements the `render()` method:

```python
from dash import html
from templates.pages import Page


class SalesPage(Page):
    def render(self):
        return html.Div([
            html.H3("Sales"),
            html.P("Sales page content"),
        ])
```

### 3. Register the Page in the Sidebar

Add a corresponding entry to `DashboardConfig.SIDEBAR_ITEMS` in `config.py`:

```python
{"name": "Sales", "id": "sales"}
```

## AutoGrid Guide

`AutoGrid` automatically arranges charts into rows and columns based on their IDs and specified dimensions. It handles the layout structure, allowing you to focus on defining charts and analyzing data rather than manually building the UI.

### Parameters

| Parameter | Description |
|---|---|
| `items` | A dictionary defining the charts, titles, and layout dimensions. |
| `container_height` | The total height of the grid container.  |
| `gap` | The spacing between rows, columns, and vertically stacked items. |

#### Defining Items

The `items` parameter is a dictionary in which each key is a **three-character grid ID**, and each value is a configuration dictionary.

##### Grid ID Structure (Items Key)

Grid IDs must contain exactly three characters.

| Character | Purpose |
|---|---|
| First character | Identifies the row. |
| Second character | Identifies the column within that row. |
| Third character | Distinguishes items within the same row and column. |


##### Item Configuration (Items Value)

Each grid item requires the following configuration fields:

| Field | Description |
|---|---|
| `title` | The title displayed above the chart. |
| `fig` | A Plotly figure object displayed in the chart. |
| `width` | The column width as a relative percentage value. Column widths within each row must sum to `100`. |
| `height` | The item's height as a relative percentage value. Heights of items stacked in the same column must sum to `100`. |

**Important:** Items in the same column must use the same `width`. 



