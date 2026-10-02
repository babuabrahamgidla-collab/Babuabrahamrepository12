print("Hello, world!, 27 September evening session")
import pdfplumber
import json

input_file = r'C:\Users\babua\PycharmProjects\pythonproject02\HDFC_TDS_JAN2025.pdf'
output_file = "jsonHDFCTDS.json"
try:
    extracted_text = ""
    with pdfplumber.open(input_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            extracted_text +=text+"\n"
    json_input_data={
        "pdf_text":   extracted_text
        }
    
    with open(output_file, "w", encoding="UTF=8") as jf:
        json.dump(json_input_data, jf, indent=4)
    print("PDF is converted to json sucessfully")
        
        
except Exception as e:
    print("The exception that occured is", e)
