import json
from datetime import datetime
import csv

print("Hello World")
print("Hello World, world of files in Python, 12Sep and Sep14")

# ---------------------------------------------------------
# LOGGING FUNCTION (works perfectly)
# ---------------------------------------------------------
def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {message}\n"

    try:
        with open("log.txt", "a") as f:
            f.write(entry)
        print("Log updated")
    except Exception as e:
        print("Error writing to log:", e)

write_log("Started Python practice session")
write_log("Morning session begins")

# ---------------------------------------------------------
# INITIAL JSON CREATION
# ---------------------------------------------------------
data = {
    "date": "2026-09-14",
    "session": [],
    "tasks": ["txt files", "JSON", "CSV", "Exceptions"],
    "dog_walk": {
        "time": "10:00:00",
        "duration": 80,
        "completed": False
    }
}

try:
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
except Exception as e:
    print(e)

# ---------------------------------------------------------
# READ JSON AND PRINT DOG WALK DURATION
# ---------------------------------------------------------
try:
    with open("data.json", "r") as f:
        info = json.load(f)

    print(info["dog_walk"]["duration"])
except Exception as e:
    print(e)

# ---------------------------------------------------------
# UPDATE JSON (ADD TASK + MARK WALK COMPLETED)
# ---------------------------------------------------------
try:
    with open("data.json", "r") as f:
        data = json.load(f)

    data["tasks"].append("review")
    data["dog_walk"]["completed"] = True

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

except Exception as e:
    print(e)

# ---------------------------------------------------------
# FUNCTION: ADD TIMESTAMPED SESSION ENTRY
# ---------------------------------------------------------
def add_session(filename, message):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except Exception:
        data = {}

    if "session" not in data:
        data["session"] = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "time": timestamp,
        "message": message
    }

    data["session"].append(entry)

    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Session added.")
    except Exception as e:
        print("Error saving session:", e)

# Example usage:
add_session("data.json", "Completed JSON practice block.")
add_session("data.json", "Reviewed code and added timestamps.")

rows =[
    ["tasks", "hours"], 
    ["Python practicve", 3],
    ["dog_walk", 1.33],
    ["review", .5]
    
]
with open("schedule.csv", "w", newline="") as f:
    writer=csv.writer(f)
    writer.writerows(rows)
    
print("schedule.csv file is written successfully")

with open("schedule.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
new_row = ["break", 1]        
with open("schedule.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_row)
print("New row is added")

total=0
with open("schedule.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        task = row[0]
        hours = float(row[1])
        total += hours

print("Total hours:", total)

def add_csv_entry(task, hours):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row =[task, hours, timestamp]
    
    try:
        with open("schedule.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)
        print("CSV entry added")
    except Exception as e:
        print("Error writing to csv ", e)
add_csv_entry("Python practice", 6)
add_csv_entry("evening walk", 1.5)    


