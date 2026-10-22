import numpy as np
import pandas as pd

import plotly
import plotly.graph_objects as go
import plotly.express as px


#==========================================
# config
#==========================================

CHARTS = {
    'color_palette' : plotly.colors.sequential.Blues,
    'color': '#4169E1',
    'fill_color':'rgba(65, 105, 225, 0.2)',
    'text_color':'white',
    'opacity':0.5,
    'line_width':3,
    'font_family':"-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Vazirmatn', 'Vazir', 'IRANSans', 'Tahoma', sans-serif",

}


#==========================================
# bar plot
#==========================================

def create_bar_chart(x, y, data=None):
    
    if data:
        x=data[x]
        y=data[y]

    fig = go.Figure(data=[
        go.Bar(
            x=x,
            y=y,
            marker_color = CHARTS['fill_color'],
                # Another Options :
                ### 1. "Red"
                ### 2. plotly.colors.sequential.Plotly3
                ### 3. px.colors.qualitative.Pastel
                ### 4. ["#ec4899", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ef4444"]
                ### 5. ['#ec4899' if val>30 else '#3b82f6' for val in y]
                ### 6. "rgb(158,202,225)"
                ### 7. "rgba(158,202,225,0.1)"

            marker_line_color=CHARTS['color'],
            marker_line_width = CHARTS['line_width'],
            #opacity=CHARTS['opacity'],
            #text=[f"{val:,.0f}" for val in y], #for df: data[y_col].apply(lambda x: f"{x:,.0f}"),
            #textposition='outside',
            #textfont=dict(color='Black', size=10),
            #width=0.5,
            #hovertext=[f"{i}% market share" for i in y],

        )
    ])

    fig.update_layout(
        barcornerradius=90,
        #showlegend=True,
        #xaxis=dict(tickfont=dict(color="Red", size=10), gridcolor="Green"),
        #title= " ",
        #template="ggplot2",
    )

    return fig


#==========================================
# gauge plot
#==========================================

def create_gauge_plot(val=47, min=0, max=100):

    fig = go.Figure(data=[
        go.Indicator(
            mode="gauge+number",
            value=val,
            #title={"text": " "},
            number=dict(
                font=dict(
                    size=100,
                    color=CHARTS['color'],
                    family=CHARTS['font_family']
                )
            ),
            gauge=dict(
                axis=dict(
                    range=[min, max],
                    tickfont=dict(color=CHARTS['text_color']), 
                    tickwidth=1
                ),
                bar=dict(
                    color=CHARTS['color']
                ),

                #bgcolor="White",

                borderwidth=1.5,
                bordercolor=CHARTS['color'],

                #steps=[
                    #dict(range=[min, max/3], color="Green"),
                    #dict(range=[max/3, 2*max/3], color="Yellow"),
                    #dict(range=[2*max/3, max], color="Red")],

                #threshold=dict(line=dict(color="Blue", width=2),thickness=0.75,value=max * 0.8)
            )
        )
    ])

    return fig


#==========================================
# scatter plot
#==========================================

def create_scatter_plot(x, y, mode='markers'): 
    '''
    modes:
        1. markers
        2. lines
        3. markers+lines
    '''
    
    line=dict(
        color=CHARTS['color'],
        width=CHARTS['line_width']
    )

    marker=dict(
        color=CHARTS['color'],
        size=9
    )

    scatter_kwargs = {
        'x': x,
        'y': y,
        'mode': mode,
    }

    if mode == 'lines':
        scatter_kwargs['line'] = line
        scatter_kwargs['fill'] = 'tozeroy'
        scatter_kwargs['fillcolor'] = CHARTS['fill_color']

    elif mode == 'markers':
        scatter_kwargs['marker'] = marker

    elif mode == 'markers+lines':
        scatter_kwargs['line'] = line
        scatter_kwargs['fill'] = 'tozeroy'
        scatter_kwargs['fillcolor'] = CHARTS['fill_color']
        scatter_kwargs['marker'] = marker

    fig=go.Figure(data=[go.Scatter(**scatter_kwargs)])

    return fig


#==========================================
# pie chart
#==========================================

def create_pie_chart(labels, values, hole=0.4):

    fig=go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=hole,
            marker=dict(
                colors=[CHARTS['fill_color']] * len(labels),
                line=dict(
                    color=CHARTS['color'],
                    width=CHARTS['line_width'],
                )
            ),
            textfont=dict(
                family=CHARTS['font_family'],
                color=CHARTS['text_color'],
                size=11
            ),
            textinfo='label+percent',
            #textposition='outside',
            hoverinfo='label+percent+value',
            opacity=CHARTS['opacity'],
            pull=[0.05 if i == 0 else 0 for i in range(len(labels))]
        )
    ])

    fig.update_layout(
        showlegend=True,
        legend=dict(
            font=dict(color=CHARTS['color']),
            bgcolor='rgba(0,0,0,0)'
        )
    )

    return fig


def create_pie_chart2(labels, values, hole=0.4):
    
    # Generate a color sequence based on your primary color
    # This creates lighter/darker variations of your main color
    import colorsys
    
    # Convert hex to RGB
    hex_color = CHARTS['color'].lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    # Generate different shades of the same color
    n_colors = len(labels)
    colors = []
    for i in range(n_colors):
        # Vary the lightness (0.3 to 0.9 range)
        lightness = 0.3 + (i / n_colors) * 0.6
        # Convert RGB to HSL, adjust lightness, convert back
        hls_color = colorsys.rgb_to_hls(r/255, g/255, b/255)
        rgb_color = colorsys.hls_to_rgb(hls_color[0], lightness, hls_color[2])
        colors.append(f'rgb({int(rgb_color[0]*255)}, {int(rgb_color[1]*255)}, {int(rgb_color[2]*255)})')
    
    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=hole,
            marker=dict(
                colors=colors,  # Use generated shades instead of color_palette
                line=dict(
                    color=CHARTS['text_color'],
                    width=1.5
                )
            ),
            textfont=dict(
                family=CHARTS['font_family'],
                color=CHARTS['text_color'],
                size=11
            ),
            textinfo='label+percent',
            textposition='auto',
            hoverinfo='label+percent+value',
            opacity=CHARTS['opacity'],
            pull=[0.05 if i == 0 else 0 for i in range(len(labels))]  # Slightly pull first slice for emphasis
        )
    ])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family=CHARTS['font_family']),
        showlegend=True,
        legend=dict(
            font=dict(color=CHARTS['color']),
            bgcolor='rgba(0,0,0,0)'
        )
    )
    
    return fig


def create_pie_chart1(labels, values, hole=0.4):
    
    # Create colors with varying opacity based on your primary color
    n_colors = len(labels)
    colors = []
    for i in range(n_colors):
        # Increase opacity from 0.3 to 1.0
        opacity = 0.3 + (i / n_colors) * 0.7
        colors.append(f'rgba(65, 105, 225, {opacity})')  # RGB of #4169E1
    
    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=hole,
            marker=dict(
                colors=colors,
                line=dict(
                    color=CHARTS['text_color'],
                    width=1.5
                )
            ),
            textfont=dict(
                family=CHARTS['font_family'],
                color=CHARTS['text_color'],
                size=11
            ),
            textinfo='label+percent',
            textposition='auto',
            hoverinfo='label+percent+value',
            opacity=CHARTS['opacity']
        )
    ])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family=CHARTS['font_family']),
        showlegend=True,
        legend=dict(
            font=dict(color=CHARTS['color']),
            bgcolor='rgba(0,0,0,0)'
        )
    )
    
    return fig

#==========================================
# create plot with plotly.graph_object
#==========================================

# fig = go.Figure(data=[go.Bar()], layout=go.Layout())

#==========================================
# update pre defined figure
#==========================================

# fig = create_bar_chart(x, y)
# fig.update_traces(marker_color="rgb(158,202,225)")
# fig.update_layout(showlegend=True)

#==========================================
# templates
#==========================================
'''
templates = {
    "ggplot2": "R-style theme with grey background and white grid lines",
    "seaborn": "Python seaborn-style with white background and thin grey grid lines", 
    "plotly": "Default Plotly theme with light blue-grey background",
    "plotly_white": "Clean white background, great for reports and publications",
    "plotly_dark": "Dark theme for dashboards and presentations",
    "simple_white": "Minimalist white background with no grid lines",
    "presentation": "Optimized for slides with larger fonts and wider margins",
    "xgridoff": "Same as plotly_white but hides vertical grid lines",
    "ygridoff": "Same as plotly_white but hides horizontal grid lines", 
    "gridon": "Shows both X and Y grid lines on light background",
    "none": "No styling applied, minimal default settings"
}
'''