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
print(county[15])
county_json_list =['tb_Alameda.json','tb_Alpine.json','tb_Amador.json','tb_Butte.json','tb_Calaveras.json','tb_Colusa.json',
                   'tb_Contra Costa.json','tb_Del Norte.json','tb_El Dorado.json','tb_Fresno.json','tb_Glenn.json','tb_Humboldt.json','tb_Imperial.json','tb_Inyo.json',
                   'tb_Kern.json','tb_Kings.json','tb_Lake.json','tb_Lassen.json','tb_LA.json','tb_Madera.json','tb_Marin.json',
                   'tb_Mariposa.json','tb_Mendocino.json','tb_Merced.json','tb_Modoc.json','tb_Mono.json',
                   'tb_Monterey.json','tb_Napa.json','tb_Nevada.json','tb_Orange.json','tb_Placer.json',
                   'tb_Plumas.json', 'tb_Riverside.json', 'tb_Sacramento.json', 'tb_SanBenito.json', 'tb_SanBernardino.json',
                   'tb_SanDiego.json', 'tb_SanJoaquin.json', 'tb_SanLuisObispo.json', 'tb_SanMateo.json',
                   'tb_SantaBarbara.json', 'tb_SantaClara.json', 'tb_SantaCruz.json', 'tb_Shasta.json', 'tb_Sierra.json',
                   'tb_Siskiyou.json', 'tb_Solano.json', 'tb_Stanislaus.json', 'tb_Sutter.json', 'tb_Tehama.json',
                   'tb_Trinity.json', 'tb_Tulare.json', 'tb_Tuolumne.json', 'tb_Ventura.json', 'tb_Yolo.json',
                    'tb_Yuba.json']
print(county_json_list[15])
length_data = len(county)
print(county_json_list[37])
for i in range(56):
    folium.Marker([float(Latitude[i]), float(Longitude[i])],popup=folium.Popup(max_width=600).add_child(folium.Vega(json.load(open(county_json_list[i])), width=500, height=300))).add_to(map_osm)


iframe = map_osm.__repr__()

map_osm.save('C:\Temp/final_visul_tb.html')