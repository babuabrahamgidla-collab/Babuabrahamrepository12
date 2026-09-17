print("Hellow World, hello to json, 15Sep")
import pdfplumber
import json
import pandas as pd


def extract_clean_text(filename):
    all_pages = []
    with pdfplumber.open(filename) as pdf:
      for page_number, page in enumerate(pdf.pages, start =1):
        text = page.extract_text()
        if not text:
            continue
        lines = text.splitlines()
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped:
                cleaned_lines.append(stripped)
        all_pages.append({
            "page":page_number,
            "lines": cleaned_lines            
        })
        
    return all_pages
def save_json(data, outputfile):
    with open(outputfile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
#--------------Run Pipeline---------------------
cleaned = extract_clean_text("QTR Bonus plan.pdf")
save_json(cleaned, "bonus_plan.json")
print("JSON file created successfully.")

# Step 1 — Load JSON

with open("bonus_plan.json", "r") as f:
    data = json.load(f)
    
# Step 2 — Flatten JSON into rows
rows=[]
for page in data:
         
    page_number = page["page"]
    for i, line in enumerate(page["lines"], start=1):
        rows.append({
        "page": page_number,
        "line_number": i,
        "text": line
        })
        
# Step 3 — Convert to Excel
        
df = pd.DataFrame(rows)
df.to_excel("bonus_plan.xlsx", index=False)
        
        