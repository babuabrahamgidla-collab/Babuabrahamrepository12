print("Hello World, hello json 15Sep evening")
import json
import pandas as pd
import pdfplumber

#write a function which takes the pdf file as an argument. 
#Remove the spaces and create get page number, create clean text
# Split the text into lines and store lines in a list.
# Strip the line of empty spaces
# Store every line number and text in the lines as a doctionary, with text as list within that dictionary
def clean_text_to_get_lines(filename):
    all_pages=[]
    with pdfplumber.open(filename) as pdf:
     for page_number, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if not text:
            continue
        cleaned_lines=[]
        lines = text.splitlines()
        for line in lines:
            stripped=line.strip()
            if stripped:
                cleaned_lines.append(stripped)
                
        all_pages.append({
            "page": page_number,
            "lines":cleaned_lines
        })
        
    return all_pages
# create a json with data and output file as arguments
def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data,f, indent=4)
        
        
#-------------Run Pipeline-----------------------------------------
cleanedtext =clean_text_to_get_lines("QTR Bonus plan.pdf")
save_json(cleanedtext, "bonus_plan3.json")
print("JSON file created successfully.")
#--------flatten the json----------------------------------
rows=[]
with open("bonus_plan3.json", "r") as f:
    data=json.load(f)
   
    for page in data:
        mypage_number = page["page"]        
        for i, line in enumerate(page["lines"], start=1):
            rows.append({
                "page": mypage_number,
                "text":line 
            })

df = pd.DataFrame(rows)
df.to_excel("bonus_plan3.xlsx", index=False)
            
    
    



    