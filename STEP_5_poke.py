import sqlite3
import requests

# We don’t want to call the api more times than is necessary. Add functionality to your
# program to write the information we retrieve from the api to a table within a SQLite3
# database (only the id, name, height and weight). When asked for a pokemon, your code
# should first check if the data is in the database, and read that instead of the api if it is.

connection = sqlite3.connect("pokemon.db")
cursor = connection.cursor()


def search_pokemon(user_input):
    
    # Check if the input is empty - close application if true
    if len(user_input) == 0:
        print("Please input a name and try again!")

    # If it's not empty then do all the following code
    else:    
        try:
            format_user_input = user_input.lower()
            result = cursor.execute(f'SELECT * FROM pokemon where name="{format_user_input}"')

            pokemon_exists = result.fetchall()

            if pokemon_exists:
                print("Printing from database!\n")
                for pokemon in pokemon_exists:
                    print("Id:",pokemon[0])
                    print("Name:",pokemon[1])
                    print("Height:",pokemon[2])
                    print("Weight:",pokemon[3])
                    print('\n')
            else:
                print("Doesn't exist in the database. Let me check online!\n")
                
                response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{format_user_input}')
                result = (response.json())
                new_dict = {"id":result["id"],"name":result["name"],"height":result["height"],"weight":result["weight"]}

                cursor.execute("INSERT INTO pokemon VALUES (?, ?, ?,?)", (new_dict["id"], new_dict["name"], new_dict["height"],new_dict["weight"]))
                connection.commit()

                for key, value in new_dict.items():
                    print(key.capitalize(),":", value)
        except:
            print("Please input a valid argument!")
            print('\n')
        
        cursor.close()
        connection.close()


user_input = input("Please enter a Pokemon: ")
search_pokemon(user_input)