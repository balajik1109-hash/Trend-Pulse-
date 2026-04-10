# task4_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        # Load cleaned data
        file_path = "cleaned_trends.csv"
        df = pd.read_csv(file_path)

        print("Data loaded successfully!")

    except Exception as e:
        print("Error loading CSV:", e)
        return

    # -----------------------------
    # 1. Category Distribution (Bar Chart)
    # -----------------------------
    category_counts = df["category"].value_counts()

    plt.figure()
    category_counts.plot(kind="bar")
    plt.title("Number of Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("category_distribution.png")
    plt.show()

    # -----------------------------
    # 2. Average Score per Category
    # -----------------------------
    avg_scores = df.groupby("category")["score"].mean()

    plt.figure()
    avg_scores.plot(kind="bar")
    plt.title("Average Score per Category")
    plt.xlabel("Category")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("avg_score_category.png")
    plt.show()

    # -----------------------------
    # 3. Top 5 Posts by Score
    # -----------------------------
    top_posts = df.sort_values(by="score", ascending=False).head(5)

    plt.figure()
    plt.barh(top_posts["title"], top_posts["score"])
    plt.title("Top 5 Highest Scoring Posts")
    plt.xlabel("Score")
    plt.ylabel("Title")
    plt.tight_layout()
    plt.savefig("top_posts.png")
    plt.show()

    # -----------------------------
    # 4. Comments vs Score Scatter Plot
    # -----------------------------
    plt.figure()
    plt.scatter(df["num_comments"], df["score"])
    plt.title("Comments vs Score")
    plt.xlabel("Number of Comments")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("comments_vs_score.png")
    plt.show()

    print("\nAll charts saved in 'task3_analysis.' folder.")

if __name__ == "__main__":
    main()