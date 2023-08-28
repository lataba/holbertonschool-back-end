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
    todos = requests.get(api_url + "todos", params={"userId": employee_id}).json()

    for task in todos:
        if task.get("completed"):
            completed_task += 1
            completed_task_titles.append(task.get("title"))
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed_task, total_tasks))
    for task_title in completed_task_titles:
        print("\t {}".format(task_title))
