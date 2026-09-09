from fastapi import APIRouter, UploadFile, File
from services.bug_detector import detect_bugs
from services.security_scanner import scan_security
from services.performance_analyzer import analyze_performance
from services.ai_engine import analyze_code_ai

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    code = await file.read()
    code = code.decode("utf-8")

    bugs = detect_bugs(code)
    security = scan_security(code)
    performance = analyze_performance(code)
    ai_analysis = analyze_code_ai(code)

    return {
        "bugs": bugs,
        "security": security,
        "performance": performance,
        "ai_analysis": ai_analysis
    }
