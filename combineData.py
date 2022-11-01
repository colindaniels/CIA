import pandas
import json

import pandas as pd

filename = 'weather.json'

with open(filename, 'r') as file:
    json_data = json.loads(file.read())['data']

weather_df = pd.DataFrame(json_data)
weather_df.rename(columns={'datetime': 'Date'}, inplace=True)

crime_csv = 'chicago_crime.csv'

crime_df = pd.read_csv(crime_csv)

# include only date part of datetime
crime_df['Date'] = crime_df['Date'].str.replace('/', '-').str.split(' ').str[0]

# switch year to last index
weather_df['Date'] = ['-'.join(map(str, e)) for e in weather_df['Date'].str.split('-').str[1:] + weather_df['Date'].str.split('-').str[:1]]

weather_df['Month'] = crime_df['Date'].str.split('-').str[0]


combined_df = pd.merge(crime_df, weather_df, on='Date')

combined_df.to_csv('combined.csv')
