#this will handle the request like the api call
#what headers, url, response and stus code


import requests


def get_user_repos(token: str):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    url = "https://api.github.com/user/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception ("Failed to fetch repos")
    
    repos= response.json()
    repo_name = []
    for item in repos:
        repo_name.append(item["name"])

    return repo_name