#!/usr/bin/python3
"""
Export data in the JSON format
"""
import json
import requests


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(api_url + "users").json()

    dicti = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get(
            api_url + "todos",
            params={"userId": user_id}).json()

        dicti[user.get("id")] = [{"task": task.get("title"),
                                  "completed": task.get("completed"),
                                  "username": user.get(
                                    "username")} for task in todos]

    file_json = "todo_all_employees.json"
    with open(file_json, "w") as f:
        json.dump(dicti, f)
