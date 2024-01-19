import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/clefairy')

result = (response.json())

#Gets relevant attributes and stores them into a dict
new_dict = {"id":result["id"],"name":result["name"],"height":result["height"],"weight":result["weight"]}

print(new_dict)

