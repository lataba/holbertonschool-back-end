#!/usr/bin/python3
"""
Returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":

    completed_task = 0
    total_tasks = 0
    employee_id = argv[1]
    task_title = []

    emp_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    for task in todo_response.json():
        if task.get("completed") is True:
            completed_task += 1
            total_tasks += 1
            task_title.append(task.get("title"))
        else:
            total_tasks += 1

    name = emp_response.json()["name"]

    print("Employee {} is done with tasks({}/{}):".
          format(name, completed_task, total_tasks))

    for task in task_title:
        print("\t {}".format(task))
