#!/usr/bin/python3
'''
data in the JSON format
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    userid = argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(userid)
    user_data = requests.get(url_user).json()
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(userid)
    todo_data = requests.get(url_todo).json()
    
    username = user_data.get('username')
    
    tasks = [{"task": task.get("title"),
              "username": username,
              "completed": task.get("completed")} for task in todo_data]
    
    json_data = {}
    json_data[userid] = tasks
    
    with open("{}.json".format(userid), 'w') as json_file:
        json.dump(json_data, json_file)
