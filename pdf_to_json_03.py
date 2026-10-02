print("Hello, world!, 27 September, evening session")
import pdfplumber
import json
input_file = "ClubAgreement.pdf"
output_file="Club_agreement_in_json.json"

try:
    extracted= ""
    with pdfplumber.open(input_file) as pdf:
        for page in pdf.pages:
            extract= page.extract_text()
            extracted += extract+"\n"
    #print(extracted)
    
    data = {
        "pdf_text": extracted
    } 
    
    with open(output_file, "w", encoding="UTF-8") as jf:
        json.dump(data, jf, indent=4)
    print("json file is created successfully")       
            
       
except Exception as e:
    print("The exception is: ", e)