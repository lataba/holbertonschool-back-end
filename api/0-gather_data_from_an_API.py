#!/usr/bin/python3
"""
Returns a list information for a given ID
"""

import requests
from sys import argv

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        api_url + "users/{}".format(argv[1])).json()
    todo_tasks = requests.get(
        api_url + "todo_tasks",
        params={"userId": sys.argv[1]}).json()

    completed_task = []
    for task in todo_tasks:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todo_tasks)))
    for complete in completed_tasks:
        print("\t {}".format(complete))
