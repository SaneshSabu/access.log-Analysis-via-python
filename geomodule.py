import requests

def geolocation(ip=None,api_key=None):

  if ip != None and api_key != None:
    
    return requests.get("https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}".format(api_key,ip)).json()['country_name']
  
  else:
        
    return None
