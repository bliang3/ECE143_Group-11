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
county_json_list =['temp_Alameda.json','temp_Alpine.json','temp_Amador.json','temp_Butte.json','temp_Calaveras.json','temp_Colusa.json',
                   'temp_Contra Costa.json','temp_Del Norte.json','temp_El dorado.json','temp_Fresno.json','temp_Glenn.json','temp_Humboldt.json','temp_Imperial.json','temp_Inyo.json',
                   'temp_Kern.json','temp_Kings.json','temp_Lake.json','temp_Lassen.json','temp_LA.json','temp_Madera.json','temp_Marin.json',
                   'temp_Mariposa.json','temp_Mendocino.json','temp_Merced.json','temp_Modoc.json','temp_Mono.json',
                   'temp_Monterey.json','temp_Napa.json','temp_Nevada.json','temp_Orange.json','temp_Placer.json',
                   'temp_Plumas.json', 'temp_Riverside.json', 'temp_Sacramento.json', 'temp_SanBenito.json', 'temp_SanBernardino.json',
                   'temp_SanDiego.json', 'temp_SanJoaquin.json', 'temp_SanLuisObispo.json', 'temp_SanMateo.json',
                   'temp_SantaBarbara.json', 'temp_SantaClara.json', 'temp_SantaCruz.json', 'temp_Shasta.json', 'temp_Sierra.json',
                   'temp_Siskiyou.json', 'temp_Solano.json', 'temp_Stanislaus.json', 'temp_Sutter.json', 'temp_Tehama.json',
                   'temp_Trinity.json', 'temp_Tulare.json', 'temp_Tuolumne.json', 'temp_Ventura.json', 'temp_Yolo.json',
                    'temp_Yuba.json']
print(county_json_list[15])
length_data = len(county)
print(county_json_list[37])
for i in range(56):
    folium.Marker([float(Latitude[i]), float(Longitude[i])],popup=folium.Popup(max_width=600).add_child(folium.Vega(json.load(open(county_json_list[i])), width=500, height=300))).add_to(map_osm)


iframe = map_osm.__repr__()

map_osm.save('C:\Temp/final_visul_temp.html')