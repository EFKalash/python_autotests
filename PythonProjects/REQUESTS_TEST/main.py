import requests

token = '681fb032caeb223abd66a919dc46d80b'
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Бульба",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_add_pokemon.text)


response_change_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "20854",
    "name": "Бульба1",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_change_pokemon.text)


response_add_pokeball_pokemon = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "20856"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})

print(response_add_pokeball_pokemon.text)