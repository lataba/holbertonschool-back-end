#!/usr/bin/python3
"""
Returns information about his/her TODO list progress
"""
import requests
from sys import argv

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        api_url + "users/{}".format(argv[1])).json()
    todos = requests.get(
        api_url + "todos",
        params={"userId": argv[1]}).json()

    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for complete in completed:
        print("\t {}".format(complete))
