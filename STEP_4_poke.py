import requests
import sys

# Add the functionality to your code to accept arguments from the command line. The input
# to the command line should look something like ‘python poke.py pikachu’ and the returned
# value should be the dictionary for that pokemon.


def search_pokemon(user_input):

    format_user_input = user_input.lower()

    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{format_user_input}')
        result = (response.json())

        new_dict = {"id":result["id"],"name":result["name"],"height":result["height"],"weight":result["weight"]}

        print("\n")
        print(new_dict)
        print("\n")

    except:
        print("\n")
        print("Sorry, that Pokemon does not exist!")
        print("\n")


# Get the first element for the user input
user_input = sys.argv[1]

search_pokemon(user_input)