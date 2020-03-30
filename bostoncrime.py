# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import geopandas as gpd
import folium
from folium import Marker,Circle,Choropleth
from folium.plugins import HeatMap, MarkerCluster
import numpy as np
import pandas as pd
import math
def embed_map(m,file_name):
    from IPython.display import IFrame
    m.save(file_name) 
    return IFrame(file_name,width='100%',height='500px')
m_1=folium.Map(location=[42.32,-71.0589],tiles='openstreetmap',zoom_control=10)
embed_map(m_1,'m_1.html')
df = pd.read_csv('crime.csv',encoding='latin-1')
daytime_robberies = df[((df.OFFENSE_CODE_GROUP=='Robbery') & \
                      (df.HOUR.isin(range(9,18))))]
daytime_robberies.dropna(subset=['Lat', 'Long', 'DISTRICT'], inplace=True)
daytime_robberies.dropna(subset=['Lat', 'Long', 'DISTRICT'], inplace=True)
m_2=folium.Map(location=[42.32,-71.0589],tiles='cartodbpositron',zoom_control=13)

for idx, row in daytime_robberies.iterrows():
    Marker([row['Lat'],row['Long']]).add_to(m_2)
embed_map(m_2,'m_2.html')

m_3 = folium.Map(location=[42.32,-71.0589],tiles='cartodbpositron',zoom_control=13)

mc = MarkerCluster()
for idx, row in daytime_robberies.iterrows():
     if not math.isnan(row['Long']) and not math.isnan(row['Lat']):
        mc.add_child(Marker([row['Lat'], row['Long']]))
m_3.add_child(mc)

embed_map(m_3,'m_3.html')
