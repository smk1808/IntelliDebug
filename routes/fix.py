from fastapi import APIRouter, UploadFile, File
from services.code_fixer import fix_code

router = APIRouter()

@router.post("/fix")
async def fix(file: UploadFile = File(...)):

    code = await file.read()
    code = code.decode("utf-8")
    fixed = fix_code(code)

    return {
        "result": fixed
    }
