import pandas as pd
import xmltodict
import json

with open('melbourneObservations.xml', 'r') as file:
    xml_content = file.read()

xmlDictionary = xmltodict.parse(xml_content)
json_data = json.dumps(xmlDictionary, indent=4)

with open("melbourneObservations.json", "w") as json_file:
    json_file.write(json_data)

#GIT TEST