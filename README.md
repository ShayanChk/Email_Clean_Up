# Email Validation Script
This is a Python script, which I wrote in Jupyter for cleaning up the clients's emails. The CSV file has been extracted from the database, which contains the client's email. It checks for the presence of the '@' symbol in email addresses column from a CSV file and flags entries that are missing this symbol. It performs the following steps:

## 1. Define the Function:

check_for_at_symbol(email): This function checks if an email is not empty and does not contain the '@' symbol. If the '@' symbol is missing, it returns 1 to flag the entry; otherwise, it returns 0.


## 2. Load the CSV File:
The script loads the CSV file into a Pandas DataFrame. The file is assumed to be named Emails.csv.

## 3. Apply the Function:

The script applies the check_for_at_symbol function to the "Primary Email" and "Other Email" columns in the DataFrame. It creates a new column, Check for @, that contains 1 if either email column is missing the '@' symbol, and 0 otherwise.

## 4. Save the Updated DataFrame:

The script saves the updated DataFrame back to a new CSV file named emails_checked.csv.
