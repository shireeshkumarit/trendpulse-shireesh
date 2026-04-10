import requests
import pandas as pd
import json
from datetime import datetime
import time
import os

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

try:

  response = requests.get(url, headers=headers)
  top_stories = response.json()
  print(type(top_stories))
  top_stories_500 = top_stories[:500]
  print(top_stories_500)
except Exception as e:
  print("error occured while getting the Top stories IDs",e)
  exit()
# top 500 stories


stories_by_category = []
for id in top_stories_500:
  response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json', headers=headers)
  story = response.json()
  # print(story)
  for category, keywords in categories.items():
    # print(f"Category: {category}, Keyword : {keywords}")
    for keyword in keywords:
      # print(keyword.lower())
      # print(story.get("title").lower())
      if keyword.lower() in story.get("title").lower():
        # print(keyword)
        stories_by_category.append({
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": category,
            "score": story.get("score"),
            "num_comments": story.get("descendants"),
            "author": story.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        })
  # time.sleep(0.5)
  
  # data = json.loads(stories_by_category)
  # print(json.dumps(data,indent=2))
  # print(stories_by_category)
  
# print(json.dumps(stories_by_category, indent=2))
