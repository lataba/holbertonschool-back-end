#!/usr/bin/python3
"""
Export data in the JSON format
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(
        api_url + "users/{}".format(argv[1])).json()
    todos = requests.get(
        api_url + "todos",
        params={"userId": argv[1]}).json()

    dicti = {user.get("id"): [{"task": task.get("title"),
                               "completed": task.get("completed"),
                               "username": user.get(
                                "username")} for task in todos]}

    file_json = argv[1] + ".json"
    with open(file_json, "w") as f:

        json.dump(dicti, f)
