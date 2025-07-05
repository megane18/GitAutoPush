from fastapi import APIRouter

roter = APIRouter()


router.get("/repos")
def get_repos():
    return {"repos": ["repo1","repo2"]}