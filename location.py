import urllib.request
import json


API_KEY = 'insert API key here'
URL = f'https://geo.ipify.org/api/v2/country,city?apiKey={API_KEY}&format=json'


def access():
    request = urllib.request.Request(URL, data = None)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    response.close()
    data = json.loads(response_data)
    return data['location']['lat'], data['location']['lng']
