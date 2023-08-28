#!/usr/bin/python3
"""
Returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    completed_task = 0
    total_tasks = 0
    completed_task_titles = []

    api_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(api_url + f"users/{employee_id}").json()
    todo_list = requests.get(api_url + f"users/{employee_id}/todos").json()

    for task in todo_list:
        if task.get("completed"):
            completed_task += 1
            completed_task_titles.append(task.get("title"))
        total_tasks += 1

    name = user.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_task, total_tasks))
    for task_title in completed_task_titles:
        print("\t {}".format(task_title))
