from pydantic import BaseModel


#so this tells us what repo, file, and branch to commit to
class RepoConfig(BaseModel):
    repo_name: str
    branch: str ="main"
    #reason is because I intend for the daily commit to be .txt file
    file_path: str


#this is if they run out of the content withint the .txt file
#they can go to that fall back if they enable it, and it will give them a grace period
#and notify them
class FallBackSettings(BaseModel):
    fallback_mode: str ="smart" #or pause or none
    grace_days: int = 2
    notify_on_fallback: bool = True


class CommitPayload(BaseModel):
    content: str
    commit_message: str
    source_content: str ="quote" #can be problem or anything


#this is to make it dynamic so others can use it
#without needing to modify the .env
class GithubToken(BaseModel):
    token: str