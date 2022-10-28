import pandas as pd
import matplotlib

filename = "chicago_crime.csv"

data = pd.read_csv(filename)

arrest_groupby = data.groupby(['Domestic'])
arrest_data = {
    "Total Count": arrest_groupby.nunique()['ID']
}

df = pd.DataFrame(arrest_data)
print(df.to_string())
