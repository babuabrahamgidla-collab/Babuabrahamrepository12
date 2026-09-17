print("Hello world, hello json, 15Sep afternoon")
import json
import pandas as pd
import pdfplumber
#TCreate a function to extract clean text. Read input pdf file, one page at at time, take contents into text.
# Split the text into lines, store each line to a list with name lines. 
# Remove the empty spacces, use the method strip(). Store the stripped lines to a list with name cleaned_lines
# Do same for all pages, that is use a for loop, take each i as page number.  

def extract_clean_text(filename):
    all_pages = []
    with pdfplumber.open(filename) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if not text:
                continue
            lines = text.splitlines()
            cleaned_lines =[]
            for line in lines:
                stripped = line.strip()
                if stripped:
                    cleaned_lines.append(stripped)
            all_pages.append({
                "page": page_number,
                "lines":cleaned_lines
            })
            
    return all_pages
# Create a method to take data and filename as arguments to create a json file
# open the file in write mode, do json.dump
def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        
#--------------Run Pipeline---------------------

cleaned = extract_clean_text("QTR Bonus plan.pdf")
save_json(cleaned, "bonus_plan2.json")
print("JSON file created successfully.")
# Step 1 — Load JSON
        
with open("bonus_plan2.json", "r") as f:
    data = json.load(f)
    
# Step 2 — Flatten JSON into rows
rows =[]
for page in data:
    page_number =page["page"]
    for i, line in enumerate(page["lines"], start=1):
        rows.append({
            "page":page_number,
            "line": i,
            "text": line           
            
        })
# Step 3 — Convert to Excel   
    
df = pd.DataFrame(rows)
df.to_excel("bonus_plans.xlsx", index=False)
        
        
 