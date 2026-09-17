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
