# task3_analysis.py

import pandas as pd
import numpy as np

def main():
    try:
        # Step 1: Load cleaned CSV from Task 2
        file_path = "cleaned_trends.csv"
        df = pd.read_csv(file_path)

        print("Data loaded successfully!")
        print("Shape:", df.shape)

    except Exception as e:
        print("Error loading CSV:", e)
        return

    # Step 2: Basic Info
    print("\n--- Basic Info ---")
    print(df.head())
    print(df.info())

    # Step 3: Category Distribution
    print("\n--- Category Distribution ---")
    category_counts = df["category"].value_counts()
    print(category_counts)

    # Step 4: Average Score per Category
    print("\n--- Average Score per Category ---")
    avg_scores = df.groupby("category")["score"].mean()
    print(avg_scores)

    # Step 5: Top 5 Highest Scoring Posts
    print("\n--- Top 5 Highest Scoring Posts ---")
    top_posts = df.sort_values(by="score", ascending=False).head(5)
    print(top_posts[["title", "category", "score"]])

    # Step 6: Most Active Authors
    print("\n--- Most Active Authors ---")
    top_authors = df["author"].value_counts().head(5)
    print(top_authors)

    # Step 7: NumPy Analysis (extra marks)
    print("\n--- NumPy Analysis ---")
    scores_array = np.array(df["score"])

    print("Max score:", np.max(scores_array))
    print("Min score:", np.min(scores_array))
    print("Average score:", np.mean(scores_array))
    print("Standard deviation:", np.std(scores_array))

    # Step 8: Category with highest average score
    best_category = avg_scores.idxmax()
    print("\nCategory with highest average score:", best_category)

if __name__ == "__main__":
    main()