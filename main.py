import pandas as pd
import matplotlib
import json
import csv

filename = "combined.csv"

data = pd.read_csv(filename)

df = pd.DataFrame({
    'ID': data['ID'],
    'Date': data['Date'],
    'Month': data['Month'],
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

# to float
assult_df['Max Temp'] = assult_df['Max Temp']

print(assult_df['Max Temp'])

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
                'Date': row['Date'],
                'Month': row['Month'],
                'Block': row['Block'],
                'Description': row['Description'],
                'Location Description': row['Location Description'],
                'Arrest': row['Arrest'],
                'Domestic': row['Domestic'],
                'Clouds': row['Clouds'],
                'Max Temp': float(row['Max Temp']),
                'Min Temp': float(row['Min Temp']),
                'Max Wind Speed': row['Max Wind Speed'],
                'Precipitation': row['Precipitation']
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [float(row['Longitude']), float(row['Latitude'])]
            }

        })

with open('assaults.geojson', 'w+') as file:
    json.dump(geojson, file)




#assult_df.to_json('assult.json', orient='records')