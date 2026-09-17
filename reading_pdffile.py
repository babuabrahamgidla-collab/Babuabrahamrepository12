print("Hello World, OPPs, Python and pdf, 14 Sep")

import pdfplumber

def extract_pdf_text(filename):
    full_text = ""
    try:
        with pdfplumber.open(filename) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                full_text += page_text + "\n"
        return full_text
    except Exception as e:
        print("Error:", e)
        return ""

# Example:
text = extract_pdf_text("QTR Bonus plan.pdf")
print(text)

def read_clean_pdf(filename):
    with pdfplumber.open(filename) as pdf:
       for page in pdf.pages:
           text = page.extract_text()
           if text:
                cleaned = "\n".join(
                    line.strip()
                    for line in text.splitlines()
                    if line.strip()                    
                )
                print(cleaned)
                print("\n" + "-"*50 + "\n")
                
#read_clean_pdf("QTR Bonus plan.pdf")

def read_clean_pdf(filename):
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Remove extra spaces
                cleaned = re.sub(r'\s+', ' ', text)
                print(cleaned)
                print("\n" + "-"*50 + "\n")

#read_clean_pdf("QTR Bonus plan.pdf")                      
def save_clean_pdf(filename, output_file):
    full_text = ""
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                cleaned = "\n".join(
                    line.strip()
                    for line in text.splitlines()
                    if line.strip()
                )
                full_text += cleaned + "\n\n"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_text)

save_clean_pdf("QTR Bonus plan.pdf", "clean_bonus_plan.txt")
