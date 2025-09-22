from scripts.etl import extract
import logging

EXCEL_FILE = "data/superstore.xlsx"

# Extract data
orders_df, returns_df, people_df = extract.extract(EXCEL_FILE)

# Print first 5 rows for verification
print("Orders Sample:")
print(orders_df.head())
print("\nReturns Sample:")
print(returns_df.head())
print("\nPeople Sample:")
print(people_df.head())