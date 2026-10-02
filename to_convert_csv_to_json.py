print("Hello, world!, 27 September")
{
  "tool_uses": [
    {
      "recipient_name": "functions.search_uploaded_documents",
      "parameters": {}
    }
  ]
}

import csv
import json

csv_file = r"C:\Users\babua\PycharmProjects\pythonproject02\CSV_Microsoft_comma_separated_values_for learning.csv"
json_file = r"C:\Users\babua\PycharmProjects\pythonproject02\materials.json"

try:
    data_list = []

    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # Optional cleanup: remove commas from numeric fields
            if "Price" in row:
                row["Price"] = row["Price"].replace(",", "")

            data_list.append(row)

    with open(json_file, mode="w", encoding="utf-8") as jf:
        json.dump(data_list, jf, indent=4)

    print("CSV converted to JSON successfully.")

except FileNotFoundError:
    print("CSV file not found.")
except Exception as e:
    print("Error while converting CSV to JSON:", e)
