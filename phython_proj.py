#Project Phython
import requests
import json
import pandas as pd
import pandas as pd
api_url='https://app.ticketmaster.com/discovery/v2/events.json?apikey=KLKnn1GAIKzSJGUcnUj0Y3tRhipGDKry'
response_API = requests.get(api_url)
data = response_API.text
parse_json = json.loads(data)
print(pd.json_normalize(response_API))
df=pd.DataFrame(response_API)
print (df)
#df2=pd.read_json(response_API,orient='index')
#print (df2)
#Second Phython file
pip install kaggle
import os
print(os.name)
os.getcwd()
import opendatasets as od 
import pandas as pd
od.download("https://www.kaggle.com/datasets/muratkokludataset/acoustic-extinguisher-fire-dataset") 
od.download("https://www.kaggle.com/datasets/jamesvandenberg/renewable-power-generation/Continent_Consumption_TWH.csv")
file=("top20CountriesPowerGeneration.csv")
newdata=pd.read_csv(file)
newdata
