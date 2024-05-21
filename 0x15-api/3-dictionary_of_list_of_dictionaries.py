#!/usr/bin/python3
'''
data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_data = requests.get(users_url).json()
    
    user_dict = {}
    username_dict = {}
    
    for user in users_data:
        user_id = user.get("id")
        user_dict[user_id] = []
        username_dict[user_id] = user.get("username")
    
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_data = requests.get(todos_url).json()
    
    for todo in todos_data:
        user_id = todo.get("userId")
        user_dict[user_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username_dict.get(user_id)
        })
    
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_dict, json_file)
