from fastapi import APIRouter, Depends, HTTPException
from services.github_service import get_user_repos
from app.config import settings
from db.memory_store import set_token
from app.models import GithubToken

router = APIRouter()


@router.get("/repos")
async def list_repos():
    token=settings.github_token
    repos=get_user_repos(token)
    return {"repos": repos}

@router.post("/connect")
async def connect_github(token_data: GithubToken):
    #this will get the actual styring from the pydantic model
    set_token(token_data.token)
    return {"message": "New GitHub token has been set."}

# @router.get("/results/{result_id}")
# def get_result(result_id):
#     print(f"Fetching result for: {result_id}")
#     return {"result_id": result_id}
