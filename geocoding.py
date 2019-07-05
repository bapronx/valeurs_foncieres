# coding: utf8
"""
Geocoding script that transforms a series of addresses in GPS WSG84

author:bapronx
"""


import requests
import urllib.parse as parse
import json


#load user key
keyfile = "maquest.key"
with open(keyfile, 'r') as f :
    key = f.read().strip()

print("Loaded key : {}".format(key))
url = "http://www.mapquestapi.com/geocoding/v1/batch"
#data = {'location':["France, JASSERON , 01250,  SOUS LE BOIS GIROUD","France, Paris, 75009, 44 rue de dunkerque"], 'maxResults':1, 'key':key}

def submit_data(locations):
    """ Use mapquest api to request GPS coordinates from the address
    """
    req = requests.get(url, params=locations)
    return json.loads(req.text)['results']

def  line_to_location_string(serie):
  number = serie["No voie"]
  if number.is_integer():
    number = str(int(number))
  else:
    number = ""
  return ", ".join(["France", \
      serie["Commune"], \
      ("%05i" % (serie["Code postal"],)), \
        " ".join([ number, serie["Type de voie"], serie["Voie"]])])

def get_all_location_string(df):
  location = df.apply(line_to_location_string, axis=1)
  return location.unique()

from exploration import df
toto = get_all_location_string(df)
toto