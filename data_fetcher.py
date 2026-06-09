import os
import requests
from dotenv import load_dotenv

URL = "https://api.api-ninjas.com/v1/animals"
load_dotenv()
API_KEY = os.getenv("API_KEY", "")

def get_animals_from_api(animal_name):
    """ Gets animals from api """
    parameters = { "name" : animal_name }
    try:
        response = requests.get(URL,params=parameters, headers={"X-Api-Key": API_KEY})
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return []


def serialize_animals(animals : str):
    """ Serializes animals and their info """
    output = '<li class="cards__item">'

    if "name" in animals:
        output += f'<div class="card__title">{animals["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if 'taxonomy' in animals and 'kingdom' in animals["taxonomy"]:
        kingdom = animals["taxonomy"]["kingdom"]
        output+= f'       <strong>Kingdom:</strong> {kingdom}<br/>\n'

    if 'taxonomy' in animals and 'scientific_name' in animals["taxonomy"]:
        scientific_name = animals["taxonomy"]["scientific_name"]
        output += f'      <strong>Scientific name:</strong> {scientific_name}<br/>\n'

    if "characteristics" in animals and"diet" in animals["characteristics"]:
        diet = animals["characteristics"]["diet"]
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    if "locations" in animals and len(animals["locations"])>0:
        output += f'      <strong>Location:</strong> {animals["locations"][0]}<br/>\n'

    if "characteristics" in animals and "type" in animals["characteristics"]:
        animal_type = animals["characteristics"]["type"]
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += "</li>\n"
    return output