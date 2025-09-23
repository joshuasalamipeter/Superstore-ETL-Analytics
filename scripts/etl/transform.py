import pandas as pd
import logging

def transform(orders_df, returns_df, people_df):
    logging.info("Starting data transformation...")

    # Customers Table
    customers_df = orders_df[
        ['Customer ID', 'Customer Name', 'Segment', 'Postal Code', 'City', 'State', 'Country']
    ].drop_duplicates().reset_index(drop=True)
    customers_df = customers_df.rename(columns={'Customer ID': 'CustomerID'})
    logging.info(f"Customers table created: {len(customers_df)} unique customers")

    # Products Table
    products_df = orders_df[
        ['Product ID', 'Product Name', 'Sub-Category', 'Category']
    ].drop_duplicates().reset_index(drop=True)
    products_df = products_df.rename(columns={'Product ID': 'ProductID'})
    logging.info(f"Products table created: {len(products_df)} unique products")

    # Markets Table
    markets_df = orders_df[['Market', 'Region']].drop_duplicates().reset_index(drop=True)
    markets_df['MarketID'] = markets_df.index + 1  # Create MarketID
    logging.info(f"Markets table created: {len(markets_df)} unique markets")

    # Orders Table 
    orders_table = orders_df.merge(markets_df, on=['Market', 'Region'], how='left')
    orders_table = orders_table.rename(columns={
        'Row ID': 'RowID',
        'Order ID': 'OrderID',
        'Customer ID': 'CustomerID',
        'Product ID': 'ProductID',
    })[
        ['RowID', 'OrderID', 'Order Date', 'Ship Date', 'Ship Mode',
         'CustomerID', 'ProductID', 'MarketID',
         'Sales', 'Quantity', 'Discount', 'Profit',
         'Shipping Cost', 'Order Priority']
    ]
    logging.info(f"Orders table created: {len(orders_table)} rows")

    # Returns Table
    returns_table = returns_df.rename(columns={'Order ID': 'OrderID'})
    returns_table = returns_table[['OrderID', 'Returned']]  
    logging.info(f"Returns table created: {len(returns_table)} rows")

    # People Table 
    people_table = people_df.rename(columns={'Person': 'SalesRep'})
    people_table = people_table[['SalesRep', 'Region']]
    logging.info(f"People table created: {len(people_table)} rows")

    logging.info("Data transformation complete.")

    return customers_df, products_df, markets_df, orders_table, returns_table, people_table
