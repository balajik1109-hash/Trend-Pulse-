# task2_data_cleaning.py

import json
import pandas as pd
import os

def main():
    # Step 1: Load JSON file
    try:
        # Make sure filename matches your Task 1 output
        file_path = "data/trends_20260410.json"
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print(f"Loaded {len(data)} records from JSON file.")
    
    except Exception as e:
        print("Error loading JSON file:", e)
        return

    # Step 2: Convert to DataFrame
    df = pd.DataFrame(data)
    print("\nInitial DataFrame shape:", df.shape)

    # Step 3: Data Cleaning

    # Remove duplicate posts based on post_id
    df = df.drop_duplicates(subset="post_id")
    print("After removing duplicates:", df.shape)

    # Handle missing values
    df["author"] = df["author"].fillna("unknown")
    df["num_comments"] = df["num_comments"].fillna(0)
    df["score"] = df["score"].fillna(0)

    # Convert data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].astype(int)

    # Optional: Clean text (strip spaces)
    df["title"] = df["title"].str.strip()

    # Step 4: Save cleaned data to CSV
    output_path = "data/cleaned_trends.csv"

    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"\nCleaned data saved to {output_path}")
    print("Final DataFrame shape:", df.shape)

    # Preview data
    print("\nSample data:")
    print(df.head())

if __name__ == "__main__":
    main()