import json
import folium
#import vincent
import pandas as pd
import numpy as np
import os


map_osm = folium.Map([35.681229,-117.258796691895],zoom_start=6,tiles='Stamen Terrain')
ca_counties = os.path.join(r'C:\Users\Jin Park\PycharmProjects\ECE143_group_map',r'ca-counties.geojson')
folium.GeoJson(ca_counties,name='geojson').add_to(map_osm)
folium.LayerControl().add_to(map_osm)

colnames = ['county','mean_Latitude','mean_Longitude','landArea','population','density']

df = pd.read_csv('county_data.csv',names= colnames,header =0)
df.drop([37])
county = df['county']
Latitude = df['mean_Latitude']
Longitude =df['mean_Longitude']
landArea = df['landArea']
population = df['population']
density = df['density']


county_json_list =['oxy_Alameda.json','oxy_Alpine.json','oxy_Amador.json','oxy_Butte.json','oxy_Calaveras.json','oxy_Colusa.json',
                   'oxy_Contra Costa.json','oxy_Del Norte.json','oxy_Fresno.json','oxy_Glenn.json','oxy_Humboldt.json','oxy_Imperial.json','oxy_Inyo.json',
                   'oxy_jackson.json','oxy_Kern.json','oxy_Kings.json','oxy_Lake.json','oxy_Lassen.json','oxy_LA.json','oxy_Madera.json','oxy_Marin.json',
                   'oxy_Mariposa.json','oxy_Mendocino.json','oxy_Merced.json','oxy_Modoc.json','oxy_Mono.json',
                   'oxy_Monterey.json','oxy_Napa.json','oxy_Nevada.json','oxy_Orange.json','oxy_Placer.json',
                   'oxy_Plumas.json', 'oxy_Riverside.json', 'oxy_Sacramento.json', 'oxy_SanBenito.json', 'oxy_SanBernardino.json',
                   'oxy_SanDiego.json', 'oxy_SanJoaquin.json', 'oxy_SanLuisObispo.json', 'oxy_SanMateo.json',
                   'oxy_SantaBarbara.json', 'oxy_SantaClara.json', 'oxy_SantaCruz.json', 'oxy_Shasta.json', 'oxy_Sierra.json',
                   'oxy_Siskiyou.json', 'oxy_Solano.json', 'oxy_Stanislaus.json', 'oxy_Sutter.json', 'oxy_Tehama.json',
                   'oxy_Trinity.json', 'oxy_Tulare.json', 'oxy_Tuolumne.json', 'oxy_Ventura.json', 'oxy_Yolo.json',
                    'oxy_Yuba.json']
length_data = len(county)
print(county_json_list[37])
for i in range(56):
    folium.Marker([float(Latitude[i]), float(Longitude[i])],popup=folium.Popup(max_width=600).add_child(folium.Vega(json.load(open(county_json_list[i])), width=500, height=300))).add_to(map_osm)


iframe = map_osm.__repr__()

map_osm.save('C:\Temp/final_visul_oxy.html')