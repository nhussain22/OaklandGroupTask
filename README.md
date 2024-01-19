# **The Oakland Group Tech Task**

**(Repo will be set to private after it's been viewed)**

The purpose of this exercise to generate a discussion about what was learnt, and obstacles that were overcome when solving the problems. The task primarily uses languages such as **Python** and **SQL**.

### Tools Used

- VS Code
- Python 3.12
- SQLite
- SQLite3 Editor

## Breakdown of the Tasks

This exercise uses some of the Pokemon API. Link to documentation: https://pokeapi.co/docs/v2.

### *Step 1:*

Use the requests library in python to call ‘https://pokeapi.co/api/v2/pokemon/clefairy’ and
print the JSON response to console. 

`s://pokeapi.co/api/v2/move-.................i/v2/type/18/'}}], 'weight': 75}`

### *Step 2:*

Convert the response to a dictionary, and select only the ID, name, height and weight of the
pokemon. Create a dictionary containing only this information and print this to the console. 

`{'id': 35, 'name': 'clefairy', 'height': 6, 'weight': 75}`

### *Step 3:*

Instead of having the code as one script, write a function to take the name of a pokemon as
an argument, and return the appropriate dictionary for that pokemon as from step 2. You
might at this point want to make the printed output of your program a little prettier.
```
Id : 25
Name : pikachu
Height : 4
Weight : 60
```

### *Step 4:*

Add the functionality to your code to accept arguments from the command line. The input
to the command line should look something like ‘python poke.py pikachu’ and the returned
value should be the dictionary for that pokemon..

Input:

```
python3 STEP_4_poke.py pikachu
```
Output:
```
{'id': 25, 'name': 'pikachu', 'height': 4, 'weight': 60}
```

### *Step 5:*

Add functionality to your
program to write the information we retrieve from the API to a table within a SQLite3
database (only the ID, name, height and weight). When asked for a Pokemon, your code
should first check if the data is in the database, and read that instead of the API if it is.

Input (if the Pokemon exists in the database):

```
Please enter a Pokemon: Pikachu
```
Output:
```
Printing from database!

Id: 25
Name: pikachu
Height: 4
Weight: 60
```

------

Input (using the API):

```
Please enter a Pokemon: Celebi
```
Output:
```
Doesn't exist in the database. Let me check online!

Id : 251
Name : celebi
Height : 6
Weight : 50
```
------
Input (useless input):

```
Please enter a Pokemon: nav3452d
```
Output:
```
Doesn't exist in the database. Let me check online!

Please input a valid argument!
```

## Resources used

- Understanding how the API works: ***Arpan Neupane YouTube***: [link](https://www.youtube.com/watch?v=bKCORrHbutQ)
- Understand the API result: [link](https://reqbin.com/)
- Iterate through a dictionary: [link](https://realpython.com/iterate-through-dictionary-python/)
- Take command line arguments: [link](https://moez-62905.medium.com/the-ultimate-guide-to-command-line-arguments-in-python-scripts-61c49c90e0b3#:~:text=In%20Python%2C%20command%2Dline%20arguments,arguments%20passed%20to%20the%20script.)
- Understanding Try & Except: [link](https://www.w3schools.com/python/python_try_except.asp)
- Fetching info from db: [link](https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/)
- Committing to db: [link](https://stackoverflow.com/questions/45569344/how-to-tell-if-a-value-exists-in-a-sqlite3-database-python)