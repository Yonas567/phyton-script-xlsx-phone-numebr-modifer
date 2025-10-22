import pandas as pd

# ============ CONFIGURATION - CHANGE THESE VALUES ============
input_file = 'Grade-3C.xlsx'  # Change this to your file name
start_number = 900000808              # Change this to your starting phone   # Change this to your starting phone number
# ==============================================================

# Read the Excel file
df = pd.read_excel(input_file)

# Get number of rows
num_rows = len(df)

# Generate unique phone numbers for Parent Phone column
parent_phones = [f"0{start_number + i}" for i in range(num_rows)]

# Generate unique phone numbers for Parent Additional Phone column
# Continue numbering after parent phones
additional_phones = [f"0{start_number + num_rows + i}" for i in range(num_rows)]

# Update the phone columns
df['Parent Phone'] = parent_phones
df['Parent Additional Phone'] = additional_phones

# Create output filename (adds _modified before .xlsx)
output_filename = f"modified/{input_file.replace('.xlsx', '_modified.xlsx')}"
df.to_excel(output_filename, index=False)

print(f"\n✓ Successfully created {output_filename}")
print(f"✓ Updated {num_rows} rows")
print(f"✓ Parent Phone numbers: 0{start_number} to 0{start_number + num_rows - 1}")
print(f"✓ Additional Phone numbers: 0{start_number + num_rows} to 0{start_number + 2*num_rows - 1}")

