import pandas as pd
import matplotlib
import json
import csv

filename = "combined.csv"

data = pd.read_csv(filename)

df = pd.DataFrame({
    'ID': data['ID'],
    'Date': data['Date'],
    'Block': data['Block'],
    'Primary Type': data['Primary Type'],
    'Description': data['Description'],
    'Location Description': data['Location Description'],
    'Arrest': data['Arrest'],
    'Domestic': data['Domestic'],
    'Latitude': data['Latitude'],
    'Longitude': data['Longitude'],
    'Clouds': data['clouds'],
    'Max Temp': data['max_temp'],
    'Min Temp': data['min_temp'],
    'Max Wind Speed': data['max_wind_spd'],
    'Precipitation': data['precip']
})


assult_df = df.loc[df['Primary Type'] == 'ASSAULT']

# remove no location data rows
assult_df = assult_df[assult_df['Longitude'].notna()]
#print(assult_df.count())

assult_df.to_csv('assault.csv')

# to geojson for map

geojson = {
    'type': 'FeatureCollection',
    'features': []
}

with open('assault.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        geojson['features'].append({
            'type': 'Feature',
            'properties': {
                'Date': row['Date']
            },
            'goemetry': {
                'type': 'Point',
                'coordinates': [row['Longitude'], row['Longitude']]
            }

        })



with open('assults.geojson', 'w+') as file:
    json.dump(geojson, file)
    



#assult_df.to_json('assult.json', orient='records')