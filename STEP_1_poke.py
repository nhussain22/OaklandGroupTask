import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/clefairy')

result = (response.json())

print(result)