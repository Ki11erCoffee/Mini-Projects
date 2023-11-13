# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:56:02 2023
@author: Potato
"""
import pandas as pd
import pandas_bokeh
import matplotlib.pyplot as plt
import pgeocode
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
pandas_bokeh.output_notebook()
import plotly.graph_objects as go
import plotly.io as pio
import csv
"""
nomi = pgeocode.Nominatim('us')

edf = pd.read_csv('./idk.csv', sep=',',header=None, index_col=False ,names=['shipping_postal_code','orders'])
edf['Latitude'] = (nomi.query_postal_code(edf['shipping_postal_code'].tolist()).latitude)
edf['Longitude'] = (nomi.query_postal_code(edf['shipping_postal_code'].tolist()).longitude)

fig = go.Figure(data=go.Scattergeo(
        lon = edf['Longitude'],
        lat = edf['Latitude'],
        mode = 'markers',
        marker_color = edf['orders'],
        ))

fig.update_layout(
        title = 'colC Distribution',
        geo_scope='usa',
    )
fig.show()
# Save the plot as a PNG image
pio.write_image(fig, 'plot.png')

# Display a message indicating that the plot is saved
print("Plot saved as 'plot.png' in the current directory.")
"""


"""
import plotly.graph_objects as go
import plotly.io as pio

# Generate random data for the scatter plot
import random
num_points = 50
x_data = [random.uniform(0, 10) for _ in range(num_points)]
y_data = [random.uniform(0, 10) for _ in range(num_points)]

# Create a scatter plot
fig = go.Figure(data=go.Scatter(
    x=x_data,
    y=y_data,
    mode='markers',
    marker=dict(
        size=10,
        color='blue',  # Marker color
    ),
))

# Set plot title
fig.update_layout(
    title='Random Scatter Plot',
)

# Save the plot as a PNG image
pio.write_image(fig, 'plot.png')

# Display a message indicating that the plot is saved
print("Plot saved as 'plot.png' in the current directory.")
"""


import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from geopy.geocoders import Nominatim
import numpy as np

nomi = pgeocode.Nominatim('us')

edf = pd.read_csv('./Top5Zips.csv', sep=',', header=0, index_col=False, names=['shipping_postal_code', 'orders'])

# Limit each cell in the 'shipping_postal_code' column to a length of 5
edf['shipping_postal_code'] = edf['shipping_postal_code'].str.slice(0, 5)
    
edf['Latitude'] = nomi.query_postal_code(edf['shipping_postal_code'].tolist()).latitude
edf['Longitude'] = nomi.query_postal_code(edf['shipping_postal_code'].tolist()).longitude

#edf = edf[::-1]

# Remove rows with null latitude
edf = edf.dropna(subset=['Latitude'])
# Remove rows where 'orders' is 0
edf = edf[edf['orders'] != 0]

# Specify the CSV file name
csv_file = 'outputAllUSA.csv'

# Save the NumPy array to a CSV file
np.savetxt(csv_file, edf, delimiter=',', fmt='%s')

print(f'CSV file "{csv_file}" has been created.')


"""
# Create Scattergeo for Heatmap
heatmap = go.Scattergeo(
    lon=edf['Longitude'],
    lat=edf['Latitude'],
    mode='markers',
    marker=dict(
        size=10,  # Set a constant size
        color=edf['orders'],
        colorscale='Reds',  # You can choose other color scales
        colorbar=dict(title='Orders'),
        opacity=edf['orders'] / edf['orders'].max(),  # Set opacity based on 'orders' values
    ),
    text=edf['orders'],  # Assign 'orders' values to text for heatmap representation
)

# Create Scattergeo for California boundaries
california_boundaries = go.Scattergeo(
   
)

fig = go.Figure(data=[heatmap, california_boundaries])

fig.update_layout(
    title='colC Distribution (Heatmap) with California Boundaries',
    geo=dict(scope='usa'),  # Set the scope to 'usa'
)

fig.show()

# Save the plot as a PNG image
pio.write_image(fig, 'heatmap_with_boundaries.png')

# Display a message indicating that the plot is saved
print("Plot saved as 'plot.png' in the current directory.")
"""

