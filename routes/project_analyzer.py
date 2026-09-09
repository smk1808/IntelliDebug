import zipfile
import os
import tempfile

from services.bug_detector import detect_bugs
from services.security_scanner import scan_security
from services.performance_analyzer import analyze_performance


def analyze_project_zip(zip_path):
    results = []

    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        for root, dirs, files in os.walk(temp_dir):
            for file in files:

                if file.endswith(".py"):
                    file_path = os.path.join(root, file)

                    with open(file_path, "r", encoding="utf-8") as f:
                        code = f.read()

                    bugs = detect_bugs(code)
                    security = scan_security(code)
                    performance = analyze_performance(code)

                    results.append({
                        "file": file,
                        "bugs": bugs,
                        "security": security,
                        "performance": performance
                    })

    return results
