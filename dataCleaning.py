import pandas as pd
import json

with open('melbourneObservations.json', 'r') as f:
    json_data = json.load(f)

forecastData = json_data["product"]['observations']['station']

df_forecast = pd.json_normalize(forecastData, sep= '_')
 
#print(df_forecast[['@stn-name','@stn-height']])
df_forecast.style