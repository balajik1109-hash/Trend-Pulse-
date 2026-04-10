# TrendPulse   
### Real-Time Trending Data Pipeline using HackerNews API

---

## Problem Statement

Build a complete data pipeline to collect, process, analyze, and visualize real-time trending data from HackerNews.

The project involves:
- Fetching live data from an API
- Categorizing stories into predefined categories
- Cleaning and structuring the data
- Performing analysis using Pandas and NumPy
- Visualizing insights using charts

---

##  Project Overview

TrendPulse is divided into 4 main tasks:

### 🔹 Task 1: Data Collection
- Fetched top 500 stories using HackerNews API
- Extracted important fields:
  - post_id
  - title
  - category
  - score
  - num_comments
  - author
  - collected_at
- Categorized stories into:
  - Technology
  - World News
  - Sports
  - Science
  - Entertainment
- Stored data in JSON format

---

### 🔹 Task 2: Data Cleaning
- Loaded JSON data
- Removed duplicate entries
- Handled missing values
- Converted data types
- Structured data into a clean format
- Saved cleaned dataset as CSV

---

### 🔹 Task 3: Data Analysis
- Analyzed category distribution
- Calculated average score per category
- Identified top 5 highest scoring posts
- Found most active authors
- Performed statistical analysis using NumPy:
  - Mean
  - Max
  - Min
  - Standard deviation

---

### 🔹 Task 4: Data Visualization
- Created visual insights using Matplotlib:
  - Bar chart (Category distribution)
  - Bar chart (Average score per category)
  - Horizontal bar chart (Top posts)
  - Scatter plot (Comments vs Score)
- Saved all charts as PNG images

---

##  Technologies Used

- Python
- Requests (API handling)
- Pandas (data processing)
- NumPy (numerical analysis)
- Matplotlib (data visualization)
- JSON & CSV

---

##  Project Structure
trendpulse-balaji/
│
├── task1_data_collection.py
├── task2_data_cleaning.py
├── task3_analysis.py
├── task4_visualization.py
├── data/
│ ├── trends_YYYYMMDD.json
│ ├── cleaned_trends.csv
│ ├── category_distribution.png
│ ├── avg_score_category.png
│ ├── top_posts.png
│ └── comments_vs_score.png