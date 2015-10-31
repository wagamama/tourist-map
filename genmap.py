# -*- coding: utf-8 -*-
import folium
import xmltodict
import pandas as pd


TPE_COORDINATES = (25.0375167, 121.5637)

def get_map_tpe():
    return folium.Map(
            location=TPE_COORDINATES,
            zoom_start=12,
            min_lat=24.5,
            max_lat=25.5,
            min_lon=121,
            max_lon=122)

def gen_water(path): 
    map_tpe = get_map_tpe()
    water = pd.read_csv('water.csv', encoding='big5')
    for each in water.iterrows():
        lat, lon = each[1][8], each[1][9]
        map_tpe.simple_marker(
                location=(lat, lon),
                popup=each[1][1],
                clustered_marker=True)
    map_tpe.create_map(path=path)

def gen_trash_can(path):
    map_tpe = get_map_tpe()
    for i in range(1, 13):
        trash_can = pd.read_csv('trash_can{}.csv'.format(i))
        for each in trash_can.iterrows():
            lat, lon = each[1][4], each[1][3]
            map_tpe.simple_marker(
                    location=(lat, lon),
                    clustered_marker=True)
    map_tpe.create_map(path=path)

def gen_wifi(path):
    map_tpe = get_map_tpe()
    with open('freeWifi.xml') as fd:
        wifi = xmltodict.parse(fd.read())
    for each in wifi['NewDataSet']['hotspot']:
        lat, lon = each['LAT'], each['LNG']
        text = ', '.join((each['AREA'], each['HOTSPOT_NAME'], each['ADDRESS']))
        map_tpe.simple_marker(
                location=(lat, lon),
                popup=text,
                clustered_marker=True)
    map_tpe.create_map(path=path)

def gen_toilet(path):
    map_tpe = get_map_tpe()
    with open('taipeiToilet.xml') as fd:
        toilet = xmltodict.parse(fd.read())
    toilet = toilet['soap:Envelope']['soap:Body']['GetToiletResponse']['GetToiletResult']['diffgr:diffgram']
    for each in toilet['NewDataSet']['Table']:
        lat, lon = each['Lat'], each['Lng']
        text = ', '.join((each['Title'], each['Content']))
        map_tpe.simple_marker(
                location=(lat, lon),
                popup=text,
                clustered_marker=True)
    map_tpe.create_map(path=path)

def main():
    gen_water('water.html')
    gen_trash_can('trash_can.html')
    gen_wifi('wifi.html')
    gen_toilet('toilet.html')

if __name__ == '__main__':
    main()
