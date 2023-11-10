# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import plotly_express as px
import folium
from folium.plugins import HeatMap
from matplotlib import pyplot as plt
import plotly.io as pio
pio.renderers.default='browser'

df = pd.read_csv('./output.csv')

#fig = px.density_mapbox(df, lat="latitude", lon="longitude", z="value", radius=1, center=dict(lat=df.latitude.mean(),lon=df.longitude.mean()),zoom=10, mapbox_style='open-street-map',height=900)
fig = px.density_mapbox(df, lat="latitude", lon="longitude", z="value", radius=40, center=dict(lat=34.0549,lon=-118.2426),zoom=7, mapbox_style='open-street-map',height=900)
#fig.show()
#fig.write_image("yourfile.png") 


m = folium.Map(location=[df.latitude.mean(),df.longitude.mean()], zoom_start=6, control_scale=True)

map_values = df[["latitude","longitude", 'value']]
data = map_values.values.tolist()

hm = HeatMap(data, min_opacity=0.05, max_opacity=0.9, radius=25).add_to(m)

m.save("mymap.html")
print("done")
