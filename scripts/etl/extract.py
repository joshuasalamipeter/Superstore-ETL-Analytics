import pandas as pd
import logging

def extract(file_path):
    logging.info(f"Extracting data from {file_path}...")
    try:
        order_df = pd.read_excel(file_path, sheet_name = "Orders")
        return_df = pd.read_excel(file_path, sheet_name = "Returns")
        people_df = pd.read_excel(file_path, sheet_name = "People")

        logging.info(f"Extraction Successful: Order({len(order_df)} rows), Return({len(return_df)} rows), People({len(people_df)})")
        return order_df, return_df, people_df
    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        raise
    
        