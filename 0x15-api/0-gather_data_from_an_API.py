#!/usr/bin/env python3
"""Returns a todolist or something after getting id."""
import requests
import sys

url = "https://jsonplaceholder.typicode.com/users"
user = requests.get(url + f"/{sys.argv[1]}")
todos = requests.get(url + f"/{sys.argv[1]}" + "/todos")
total = 0
comp = 0
for el in todos.json() :
    if el['completed'] == True :
        comp += 1
    total += 1

print(f"Employee {user.json()['name']} is done with tasks({comp}/{total})")
for el in todos.json() :
    if el['completed'] == True :
        print("\t" + " " + f"{el['title']}")
