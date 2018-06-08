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


colnames2 = ['county','median_ph_reuslt']
df2 = pd.read_csv('ph_median_county.csv',names=colnames2,header = 0)
medain_ph = df2['median_ph_reuslt']
print(len(medain_ph))
print(len(county))
print(county[37])




county_json_list =['ph_Alameda.json','ph_Alpine.json','ph_Amador.json','ph_Butte.json','ph_Calaveras.json','ph_Colusa.json',
                   'ph_Contra Costa.json','ph_Del Norte.json','ph_Fresno.json','ph_Glenn.json','ph_Humboldt.json','ph_Imperial.json','ph_Inyo.json',
                   'ph_jackson.json','ph_Kern.json','ph_Kings.json','ph_Lake.json','ph_Lassen.json','ph_LA.json','ph_Madera.json','ph_Marin.json',
                   'ph_Mariposa.json','ph_Mendocino.json','ph_Merced.json','ph_Modoc.json','ph_Mono.json',
                   'ph_Monterey.json','ph_Napa.json','ph_Nevada.json','ph_Orange.json','ph_Placer.json',
                   'ph_Plumas.json', 'ph_Riverside.json', 'ph_Sacramento.json', 'ph_SanBenito.json', 'ph_SanBernardino.json',
                   'ph_SanDiego.json', 'ph_SanFrancisco.json', 'ph_SanJoaquin.json', 'ph_SanLuisObispo.json', 'ph_SanMateo.json',
                   'ph_SantaBarbara.json', 'ph_SantaClara.json', 'ph_SantaCruz.json', 'ph_Shasta.json', 'ph_Sierra.json',
                   'ph_Siskiyou.json', 'ph_Solano.json', 'ph_Stanislaus.json', 'ph_Sutter.json', 'ph_Tehama.json',
                   'ph_Trinity.json', 'ph_Tulare.json', 'ph_Tuolumne.json', 'ph_Ventura.json', 'ph_Yolo.json',
                    'ph_Yuba.json']
length_data = len(county)
print(county_json_list[37])
for i in range(56):
    folium.Marker([float(Latitude[i]), float(Longitude[i])],popup=folium.Popup(max_width=600).add_child(folium.Vega(json.load(open(county_json_list[i])), width=500, height=300))).add_to(map_osm)


iframe = map_osm.__repr__()

map_osm.save('C:\Temp/final_visul_ph.html')