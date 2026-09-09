from fastapi import APIRouter
from services.github_analyzer import analyze_github_repo

router = APIRouter(tags=["GitHub Analysis"])
@router.post("/analyze-github")

def analyze_github(data: dict):
    repo_url = data["repo_url"]
    results = analyze_github_repo(repo_url)

    return {
        "files_found": len(results)
    }
