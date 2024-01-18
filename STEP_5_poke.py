import sqlite3
import requests

# We don’t want to call the api more times than is necessary. Add functionality to your
# program to write the information we retrieve from the api to a table within a SQLite3
# database (only the id, name, height and weight). When asked for a pokemon, your code
# should first check if the data is in the database, and read that instead of the api if it is.

connection = sqlite3.connect("pokemon.db")
cursor = connection.cursor()


def search_pokemon(user_input):

    format_user_input = user_input.lower()
    result = cursor.execute(f'SELECT * FROM pokemon where name="{format_user_input}"')

    record = result.fetchall()

    if record:
        for item in record:
            print("Id:",item[0])
            print("Name:",item[1])
            print("Height:",item[2])
            print("Weight:",item[3])
    else:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{format_user_input}')
        result = (response.json())
        cursor.execute("INSERT INTO pokemon VALUES (?, ?, ?,?)", (result["id"], result["name"], result["height"],result["weight"]))
        connection.commit()

        for key, value in result.items():
            print(key.capitalize(),":", value) 
    

    cursor.close()
    connection.close()


user_input = input("Please enter a Pokemon: ")
search_pokemon(user_input)