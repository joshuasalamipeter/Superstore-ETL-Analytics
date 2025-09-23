from scripts.etl import extract, transform
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

# Transform data
customers_df, products_df, markets_df, orders_table, returns_table, people_table = transform.transform(
    orders_df, returns_df, people_df
)

# Print samples
print("\nCustomers Sample:")
print(customers_df.head())

print("\nProducts Sample:")
print(products_df.head())

print("\nMarkets Sample:")
print(markets_df.head())

print("\nOrders Sample:")
print(orders_table.head())

print("\nReturns Sample:")
print(returns_table.head())

print("\nPeople Sample:")


# Saving processed tables as CSV
customers_df.to_csv("processed/customers.csv", index=False)
products_df.to_csv("processed/products.csv", index=False)
markets_df.to_csv("processed/markets.csv", index=False)
orders_table.to_csv("processed/orders.csv", index=False)
returns_table.to_csv("processed/returns.csv", index=False)
people_table.to_csv("processed/people.csv", index=False)

print("\nTransformed tables saved in /processed folder.")