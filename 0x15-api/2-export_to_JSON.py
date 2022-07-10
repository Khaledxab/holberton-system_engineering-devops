#!/usr/bin/python3
"""extend task 0"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    api_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(api_url, employee_id)
    todos_user_url = '{}/todos?userId={}'.format(api_url, employee_id)
    r_employee = requests.get(user_url).json()
    r_todos_employee = requests.get(todos_user_url).json()
    tasks_list = []
    for task in r_todos_employee:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": r_employee.get("username")
        }
        tasks_list.append(task_dict)
    json_dict = {employee_id: tasks_list}
    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
