#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        employee_id = argv[1]
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{employee_id}"
        todo_url = f"{base_url}/todos?userId={employee_id}"

        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")

        if employee_name is not None:
            todo_response = requests.get(todo_url)
            todo_data = todo_response.json()

            total_tasks = len(todo_data)
            done_tasks = [task for task in todo_data if task["completed"]]
            num_done_tasks = len(done_tasks)

            print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")
            for task in done_tasks:
                print(f"\t{task['title']}")

