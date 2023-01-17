#!/usr/bin/python3
"""
Holberton challenge
Python script that takes 2 arguments in order to solve this challenge
"""

from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    username = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    response = requests.get(url)
    for commit in response.json()[:10]:
        print(
            "{}: {}".format(
                commit['sha'], commit['commit']['author']['name']
            )
        )
