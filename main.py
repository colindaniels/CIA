import pandas as pd
import matplotlib
from geojson import Feature, FeatureCollection, Point
import json

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
print(assult_df.count())

assult_df.to_csv('assult.csv')

# to geojson for map

features = assult_df.apply(
    lambda row: Feature(geometry=Point((float(row['Longitude']), float(row['Latitude'])))),
    axis=1
).tolist()


properties = assult_df.drop(['Latitude', 'Longitude'], axis=1).to_dict('records')

feature_collection = FeatureCollection(features=features, properties=properties)

with open('assults.geojson', 'w', encoding='utf-8') as f:
    json.dump(feature_collection, f, ensure_ascii=False)


#assult_df.to_json('assult.json', orient='records')