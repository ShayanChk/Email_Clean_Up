import pandas as pd
import numpy as np

# Define the function to check for '@' symbol
def check_for_at_symbol(email):
    # Check if the email is not empty and does not contain '@'
    if pd.notna(email) and '@' not in email:
        return 1  # If '@' is missing, flag the entry
    else:
        return 0  # If '@' is present or the cell is empty, do not flag

# Loading Emails csv file into a DataFrame
df = pd.read_csv("Emails.csv")

# Applying the check for the "Primary Email" and "Other Email" columns and create "Check for @" column
df['Check for @'] = df.apply(lambda row: 1 if check_for_at_symbol(row['Primary Email']) or check_for_at_symbol(row['Other Email']) else 0, axis=1)

# Save the DataFrame back to csv file
df.to_csv('Emails_checked.csv')