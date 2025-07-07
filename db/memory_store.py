github_token = None

def set_token(token: str):
    global github_token
    github_token = token



def get_token():
    return github_token