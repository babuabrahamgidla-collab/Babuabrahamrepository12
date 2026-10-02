print("Hello, world!, 27 September afternoon session")
import pdfplumber
import json

pdf_file = r"C:\Users\babua\PycharmProjects\pythonproject02\pdf_for_learning_1.pdf"
json_file = r"C:\Users\babua\PycharmProjects\pythonproject02\pdf_tables.json"

try:
    all_tables = []

    with pdfplumber.open(pdf_file) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table_index, table in enumerate(tables, start=1):
                all_tables.append({
                    "page": page_number,
                    "table_number": table_index,
                    "rows": table
                })

    with open(json_file, "w", encoding="utf-8") as jf:
        json.dump(all_tables, jf, indent=4)

    print("Table extraction completed successfully.")

except Exception as e:
    print("Error:", e)
