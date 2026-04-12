import pandas as pd
import numpy as np

# Load Json into a Dataframe
df = pd.read_json(f"data/trends_{datetime.now().strftime('%Y%m%d')}.json")
print(f"Loaded {len(df)} stories from data/trends_{datetime.now().strftime('%Y%m%d')}.json")

# drop duplicates
df = df.drop_duplicates(subset="post_id")
print("\nAfter removing duplicates:",len(df))

# drop rows where post_id, title, or score is missing
df = df.dropna(subset = ["post_id","title","score"])
print("After removing nulls:",len(df))

#  make sure score and num_comments are integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].replace([np.inf, -np.inf], np.nan)
df["num_comments"] = pd.to_numeric(df["num_comments"], errors = "coerce").fillna(0).astype(int)

# remove stories where score is less than 5
df = df[df["score"]>=5]
print("After removing low scores:",len(df))

#  strip extra spaces from the title column
df["title"] = df["title"].str.strip()

# save to a csv file
df.to_csv("data/trends_clean.csv", index=False)
print(f"Saved {len(df)} rows to data/trends_clean.csv")

print("\n Stories per category are as follows:")
print(df.value_counts("category"))
