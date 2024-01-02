#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    user = requests.get(url + f"/{sys.argv[1]}")
    todos = requests.get(url + f"/{sys.argv[1]}" + "/todos")
    if user.status_code != 200 or todos.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)
    user_data = user.json()
    todos_data = todos.json()
    csv_filename = f"{sys.argv[1]}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            csv_writer.writerow([{user_data['id']},
                                user_data['username'],
                                todo['completed'],
                                todo['title']])
