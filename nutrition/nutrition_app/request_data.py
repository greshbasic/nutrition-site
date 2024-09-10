import requests
import json

base_url_OFF = 'https://world.openfoodfacts.net/api/v2/'
base_url_upcitemdb = 'https://api.upcitemdb.com/prod/trial/search?s='


def get_data_from_barcode(barcode):
    url = f'{base_url_OFF}/product/{barcode}'
    response = requests.get(url)
    return response.json()

def get_data_from_name(name):
    url = f'{base_url_upcitemdb}{name}&match_mode=1&type=product'
    response = requests.get(url)
    return response.json()

