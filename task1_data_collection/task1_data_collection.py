# task1_data_collection.py

import requests
import time
import json
import os
from datetime import datetime

# Base URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header (as per required)
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keywords (case-insensitive)
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def fetch_top_story_ids(limit=500):
    """Fetch top story IDs from HackerNews"""
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        response.raise_for_status()
        return response.json()[:limit]
    except Exception as e:
        print("Error fetching top stories:", e)
        return []

def fetch_story(story_id):
    """Fetch individual story details"""
    try:
        url = ITEM_URL.format(story_id)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None

def assign_category(title):
    """Assign category based on keywords"""
    if not title:
        return None
    
    title_lower = title.lower()
    
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    
    return None  # Ignore if no category matches

def main():
    # Step 1: Fetch IDs
    story_ids = fetch_top_story_ids()

    collected_data = {category: [] for category in CATEGORIES}
    
    # Step 2: Fetch stories and categorize
    for category in CATEGORIES:
        print(f"\nProcessing category: {category}")
        
        for story_id in story_ids:
            if len(collected_data[category]) >= 25:
                break
            
            story = fetch_story(story_id)
            if not story:
                continue
            
            title = story.get("title", "")
            assigned_category = assign_category(title)
            
            # Only collect if category matches
            if assigned_category == category:
                data = {
                    "post_id": story.get("id"),
                    "title": title,
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                collected_data[category].append(data)
        
        # Wait 2 seconds AFTER each category
        time.sleep(2)

    # Flatten all categories into one list
    all_stories = []
    for category in collected_data:
        all_stories.extend(collected_data[category])

    # Step 3: Save to JSON
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_stories, f, indent=4)

    print(f"\nCollected {len(all_stories)} stories. Saved to {filename}")

if __name__ == "__main__":
    main()