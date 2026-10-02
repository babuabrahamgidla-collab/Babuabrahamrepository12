print("Hello, world!, 27 September")

import json
import re

# Input JSON (from Step 1)
input_json = r"C:\Users\babua\PycharmProjects\pythonproject02\json_converted_file.json"

# Output JSON (patterns)
output_json = r"C:\Users\babua\PycharmProjects\pythonproject02\pdf_patterns.json"

try:
    # Load raw text
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        raw_text = data.get("pdf_text", "")

    # Pattern definitions
    patterns = {
        "dates": re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", raw_text),
        "emails": re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}", raw_text),
        "phones": re.findall(r"\b(?:\+?\d{1,2}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}\b", raw_text),
        "currency": re.findall(r"\$\s?\d[\d,]*\.?\d*", raw_text),
        "ssn": re.findall(r"\b\d{3}-\d{2}-\d{4}\b", raw_text),
        "zip_codes": re.findall(r"\b\d{5}(?:-\d{4})?\b", raw_text),
        "percentages": re.findall(r"\b\d+%|\b\d+\.\d+%", raw_text)
    }

    # Save extracted patterns
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=4)

    print("Pattern extraction completed successfully.")

except Exception as e:
    print("Error:", e)
