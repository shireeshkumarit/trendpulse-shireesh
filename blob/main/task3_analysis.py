import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("data/trends_clean.csv")

print("Loaded Data:",df.shape)

# First 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Shape
print("\nShape of the dataframe:", df.shape)

# Average score and comments
print("\nAverage score:", round(df["score"].mean(),2))
print("Average comments:", round(df["num_comments"].mean(),2))

print("\n--- NumPy Stats ---")
print("Mean score:", round(np.mean(df["score"]),2))
print("Median score:", round(np.median(df["score"]),2))
print("Std deviation:", round(np.std(df["score"]),2))

print("Max score:", round(np.max(df["score"]),2))
print("Min score:", round(np.min(df["score"]),2))

print("Most stories in:",df["category"].value_counts().idxmax(),df["category"].value_counts().max(),"stories")

top_story = df.loc[df["num_comments"].idxmax()]
print("Most commented story:",top_story["title"],"-", top_story["num_comments"]," comments")

# creating new columns "engagement" & "is_popular"
df["engagement"] = df["num_comments"] / (df["score"] + 1)
avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score

# save to file
df.to_csv("data/trends_analysed.csv", index=False)
print("\nSaved to data/trends_analysed.csv")
