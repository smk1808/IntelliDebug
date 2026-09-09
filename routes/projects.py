from fastapi import APIRouter, UploadFile, File
import tempfile
from services.project_summary import generate_project_summary
from services.project_analyzer import analyze_project_zip

router = APIRouter(tags=["Project Analysis"])


@router.post("/analyze-project")
async def analyze_project(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:

        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    results = analyze_project_zip(tmp_path)

    return {
        "files_scanned": len(results),
        "analysis": results
    }
