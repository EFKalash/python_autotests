import requests
import pytest

token = '681fb032caeb223abd66a919dc46d80b'
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 3687})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 3687})
    assert response.json()['trainer_name'] == 'Safary'