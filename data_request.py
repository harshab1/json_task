import json
import requests

def get_data(url):
    r = requests.get(url)
    return r.json()

def save_json(dest_file_name, data):
    with open(dest_file_name, 'w') as f:
        json.dump(data, f, indent=2)
    
