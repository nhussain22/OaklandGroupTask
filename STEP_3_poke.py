import requests

# Instead of having the code as one script, write a function to take the name of a pokemon as
# an argument, and return the appropriate dictionary for that pokemon as from step 2. You
# might at this point want to make the printed output of your program a little prettier.

def search_pokemon(x):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{x}')

    result = (response.json())

    #Gets relevant attributes and stores them into a dict
    
    new_dict = {"id":result["id"],"name":result["name"],"height":result["height"],"weight":result["weight"]}

    for key, value in new_dict.items():
        print(key, "->", value) 
    
    #print(f'The ID: {new_dict["id"]}')
    #print(f'The Name: {new_dict["name"]}')
    #print(f'The Height: {new_dict["height"]}')
    #print(f'The Weight: {new_dict["weight"]}')


search_pokemon("pikachu")