import pandas as pd
import os

# Define the directory where DVC-tracked raw data is located
DATA_DIR = 'data/raw' 

def merge_raw_data():
    """
    Loads and performs left joins on the three core Walmart data files 
    (train, features, stores) to create a single master DataFrame.
    """
    print("Starting data ingestion and merge...")

    try:
        # Load the data files
        train_df = pd.read_csv(os.path.join(DATA_DIR, 'train.csv'))
        features_df = pd.read_csv(os.path.join(DATA_DIR, 'features.csv'))
        stores_df = pd.read_csv(os.path.join(DATA_DIR, 'stores.csv'))
        
    except FileNotFoundError:
        print(f"Error: Data files not found in {DATA_DIR}. Ensure DVC pull was successful.")
        return None

    # Convert Date columns to datetime objects for accurate joining and feature creation
    train_df['Date'] = pd.to_datetime(train_df['Date'])
    features_df['Date'] = pd.to_datetime(features_df['Date'])

    # 1. Merge core sales data with store metadata (Type and Size)
    merged_data = pd.merge(
        train_df, 
        stores_df, 
        on='Store', 
        how='left'
    )
    
    # 2. Merge all features (Temperature, MarkDowns, CPI, Unemployment) 
    #    This is done on the composite key: Store, Date, and IsHoliday
    final_df = pd.merge(
        merged_data,
        features_df,
        on=['Store', 'Date', 'IsHoliday'],
        how='left',
        suffixes=('_sales', '_features') # Handles potential column overlap
    )
    
    print(f"Initial sales records: {len(train_df)}. Final merged records: {len(final_df)}.")
    
    # Save the merged raw file, ready for feature engineering
    output_path = 'data/raw/merged_sales_data.csv'
    final_df.to_csv(output_path, index=False)
    print(f"Successfully saved merged data to: {output_path}")

    return output_path


if __name__ == "__main__":
    merge_raw_data()