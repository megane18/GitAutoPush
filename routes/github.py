from fastapi import APIRouter, Depends, HTTPException
from services.github_service import get_user_repos
from app.config import settings

router = APIRouter()


@router.get("/repos")
async def list_repos():
    token=settings.github_token
    repos=get_user_repos(token)
    return {"repos": repos}
