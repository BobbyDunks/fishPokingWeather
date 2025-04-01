import pandas as pd
import json

with open('wonthaggiForecast.json', 'r') as f:
    json_data = json.load(f)

forecastData = json_data["product"]['forecast']['area']

df_forecast = pd.DataFrame(forecastData)
 
print(df_forecast)