from typing import Dict
import requests
import json


req = requests.get('https://swapi.dev/api/starships/10/')
data = json.loads(req.text)


def pilot_data_printer(pilot_info) -> None:
    for key, value in pilot_info.items():
        print('{0}: {1}'.format(key, value))
    print()


def homeworld_data(homeworld) -> str:
    homeworld_req = requests.get(homeworld)
    homeworld_data = json.loads(homeworld_req.text)

    return homeworld_data['name']


def pilots_data(pilot) -> Dict:
    pilots_parameters = ['name', 'height', 'mass']
    _data = dict()

    pilot_req = requests.get(pilot)
    pilot_data = json.loads(pilot_req.text)

    for par in pilots_parameters:
        _data[par] = pilot_data[par]
    else:
        _data['homeworld'] = homeworld_data(pilot_data['homeworld'])
        _data['homeworld_link'] = pilot_data['homeworld']

    pilot_data_printer(_data)

    return _data


def ship_data() -> Dict:
    ship_parameters = ['name', 'max_atmosphering_speed', 'starship_class']
    _data = dict()

    for par in ship_parameters:
        _data[par] = data[par]

    _data['pilots'] = list()
    for pilot in data['pilots']:
        _data['pilots'].append(pilots_data(pilot))

    return _data


with open('falcon.json', 'w') as file:
    json.dump(ship_data(), file, indent=4)
