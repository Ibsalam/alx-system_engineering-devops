#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

      print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

     [print("\t {}".format(complete)) for complete in completed]
