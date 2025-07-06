from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.github import router as github_router
# from routes.scheduler import router as scheduler_router
# from routes.fallback import router as fallback_router


app = FastAPI(
    title="GitAutoPush (GAP)",
    description="Smart commit automation for GitHub",
    version="0.1.0"
)
origins = [
     "http://localhost",
        "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def home():
    return {"message": "GitAutoPush API is live"}


app.include_router(github_router, prefix="/github", tags=["GitHub"])
# app.include_router(scheduler_router, prefix="/scheduler", tags=["Scheduler"])
# app.include_router(fallback_router, prefix="/fallback", tags=["Fallback"])
