print("Hello World, from OOPs and Python, 14Sep")

import csv
from datetime import datetime

# ---------------------------------------------------------
# 1. Create CSV with header
# ---------------------------------------------------------
def create_daily_schedule_CSV(filename):
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Task", "Hours", "Timestamp"])  # FIXED: must be a list
        print("Daily CSV tracker created")
    except Exception as e:
        print(f"This {e} had occurred")

# ---------------------------------------------------------
# 2. Add entry with timestamp
# ---------------------------------------------------------
def add_entry(filename, task, hours):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [task, hours, timestamp]  # FIXED: use list, not tuple

    try:
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)
        print("Entry added")
    except Exception as e:
        print(f"{e} had occurred")

# ---------------------------------------------------------
# 3. Read CSV
# ---------------------------------------------------------
def read_CSV(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except Exception as e:
        print("Error reading CSV:", e)

# ---------------------------------------------------------
# 4. Calculate total hours
# ---------------------------------------------------------
def total_hours(filename):
    total_hours_value = 0

    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                hours = float(row[1])  # row[1] is the Hours column
                total_hours_value += hours

        print("The total hours are:", total_hours_value)
    except Exception as e:
        print(f"The Exception {e} had occurred")
create_daily_schedule_CSV("daily_tracker.csv")
add_entry("daily_tracker.csv", "Python Practice", 1.5)
add_entry("daily_tracker.csv", "Dog Walk", 1.33)
add_entry("daily_tracker.csv", "Review", 0.5)
read_CSV("daily_tracker.csv")
total_hours("daily_tracker.csv")

        
            
          
                
        
            