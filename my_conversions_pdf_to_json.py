print("Hello, world!, 27 September, afternoon session")
import pdfplumber
import json
text=[]
pdf_file = r'C:\Users\babua\PycharmProjects\pythonproject02\Lease Application.pdf'
jsonfile = "json_converted_file"

try:
    text=""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text_extracted=page.extract_text()
            text +=text_extracted+"\n"
    #print(text)
    
    data = {
            "pdf_text": text
            }
    with open(jsonfile, "w",encoding="utf-8") as jf:
        json.dump(data, jf, indent=4)
    print("PDF converted to JSON successfully.")
                    
except Exception as e:
    print("This exception is encountered: ", e)
    
data = {
   "pdf_text": text
 }
