import pandas as pd
import matplotlib

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


