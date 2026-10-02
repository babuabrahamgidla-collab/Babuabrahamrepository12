import os

os.chdir(r"C:\Users\babua\PycharmProjects\pythonproject02")
# print("Current directory:", os.getcwd())
# print("Files here:", os.listdir())

import pandas as pd
import re

# Read the Excel file
df = pd.read_excel("pressuredrop1.xlsx", header=None)

# Assign column names
df.columns = [
    "Nominal_pipe_dia", "Sch_40_ID", "Area_ft2", "Flow_bbl_per_day",
    "Velocity_ft_per_sec", "Column_6", "Column_7", "Column_8", "Column_9",
    "Column_10", "K_value_gate_valves", "K_value_globe_valves",
    "K_value_check_valves", "K_value_plug_valves", "K_value_control_valve_Cv"
]

# Step 1: Strip whitespace
for col in df.select_dtypes(include=["object"]):
    df[col] = df[col].str.strip()

# Step 2: Extract numeric parts only from columns that are mostly numeric
for col in df.columns:
    numeric_ratio = df[col].apply(lambda x: bool(re.search(r"\d", str(x)))).mean()
    if numeric_ratio > 0.5:  # convert only if >50% of values are numeric
        df[col] = df[col].apply(
            lambda x: float(re.findall(r"\d+\.?\d*", str(x))[0]) if re.findall(r"\d+\.?\d*", str(x)) else None
        )

# Step 3: Verify
print(df.dtypes)
print(df.head())
