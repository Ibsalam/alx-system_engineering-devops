#!/usr/bin/python3
'''
export data in the JSON format
'''

import json
import requests

if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(users_url).json()

    all_tasks = {}

    for user in users_data:
        user_id = str(user['id'])
        username = user['username']
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        todo_data = requests.get(todo_url).json()

        tasks = [{"username": username,
                  "task": task["title"],
                  "completed": task["completed"]} for task in todo_data]

        all_tasks[user_id] = tasks

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_tasks, json_file)

