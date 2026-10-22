from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

import numpy as np

from templates.pages import Page
from templates.grid_system import AutoGrid
from templates.components import normalize_fig

# ----------------------------
# FIGURES
# ----------------------------
import plotly.graph_objects as go
import numpy as np

from templates.charts.charts import create_bar_chart,create_gauge_plot, create_scatter_plot,create_pie_chart

scatter = create_scatter_plot(
    x=np.linspace(0,10,50),
    y=np.sin(np.linspace(0,10,50)),
    mode='markers'
)

bar = create_bar_chart(
    x=["A","B","C","D","E","F"],
    y=[10,20,30,40,50,60]
)

'''line = px.line(
    x=[1,2,3],
    y=[3,2,5]
)'''

line = create_scatter_plot(x=[1,2,3],y=[3,2,5], mode='lines')

pie = create_pie_chart(
    labels= ['Category A', 'Category B', 'Category C', 'Category D'],
    values= [30, 25, 25, 20]
)

x = np.linspace(0, 10, 200)
y = np.exp(-((x - 5) ** 2) / 2)

kde = create_scatter_plot(x, y, mode='lines')


gauge =normalize_fig(create_gauge_plot())
gauge.update_layout(margin=dict(l=10,r=10,t=50,b=10))
gauge.update_xaxes(tickangle=90)


#3d
t = np.linspace(0,10,50)
x,y,z= np.cos(t), np.sin(t), t

scatter_3d = go.Figure(data=go.Scatter3d(x=x, y=y, z=z))


#map
df=px.data.election()
geojson=px.data.election_geojson()

map = px.choropleth_map(
    df, 
    geojson=geojson,  
    color="Bergeron", 
    locations="district", 
    featureidkey="properties.district",
    center={"lat": 45.5517, "lon": -73.7073},
    map_style="carto-positron",
    zoom=9
)

map.update_layout(
    margin={"r":0, "t":0, "l":0, "b":0}
)

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson,
    locations=df['district'],
    z=df['Bergeron'],
    colorscale="Blues",
    featureidkey="properties.district",
    marker_opacity=0.7,
    marker_line_width=0.5,
))

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=9,
    mapbox_center={"lat": 45.5517, "lon": -73.7073},
    margin={"r":0, "t":0, "l":0, "b":0}
)



# ---------------------------------
# Grid
# ---------------------------------


items = {

    "aaa": {
        "title" : "kde plot",
        "fig": normalize_fig(kde),
        "width": 40,
        "height": 40
    },

    "aab": {
        "title" : "gauge plot",
        "fig": normalize_fig(gauge),
        "width": 40,
        "height": 60
    },

    "aba": {
        "title" : "scatter plot",
        "fig": normalize_fig(scatter),
        "width": 60,
        "height": 50
    },

    "abb": {
        "title" : "line plot",
        "fig": normalize_fig(line),
        "width": 60,
        "height": 50
    },

    "baa":{
        "title" : "pie chart",
        "fig": normalize_fig(pie),
        "width": 70,
        "height": 100      
    },

    "bba":{
        "title" : "bar chart",
        "fig": normalize_fig(bar),
        "width": 30,
        "height": 100   
    },


    "daa":{
        "title" : "map",
        "fig": normalize_fig(fig),
        "width": 100,
        "height": 100       
    },
    "eaa":{
        "title" : "3d scatter plot",
        "fig": normalize_fig(scatter_3d),
        "width": 100,
        "height": 100  
    }
}


class OverviewPage(Page):
    def render(self):
        
        grid = AutoGrid(
            items,
            container_height="2500px",
            gap="15px"
        )
        return grid.build()