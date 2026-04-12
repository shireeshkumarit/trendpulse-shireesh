import pandas as pd
import matplotlib.pyplot as plt
import os

# create folder outputs
df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)

# top10 stories by score
top10 = df.sort_values("score", ascending=False).head(10)

# Horizontal bar chart
plt.barh(top10["title"].astype(str).str[:50], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# stories per category
cat_counts = df["category"].value_counts()

plt.bar(cat_counts.index, cat_counts.values, color="skyblue")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png")
plt.show()

# Scatter plot (Score vs commetns)
colors = df["is_popular"].map({True: "green", False: "red"})

plt.figure(figsize=(8,6))
plt.scatter(df["score"], df["num_comments"], c=colors, alpha=0.6)

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")

plt.legend(["Popular=Green, Not Popular=Red"])

plt.savefig("outputs/chart3_scatter.png")
plt.show()

# Dashboard
fig, axes = plt.subplots(1, 3, figsize=(18,5))

fig.suptitle("TrendPulse Dashboard", fontsize=16)

# Chart 1
axes[0].barh(top10["title"].astype(str).str[:30], top10["score"])
axes[0].set_title("Top 10 Stories")

# Chart 2
axes[1].bar(cat_counts.index, cat_counts.values, color="skyblue")
axes[1].set_title("Categories")

# Chart 3
axes[2].scatter(df["score"], df["num_comments"], c=colors)
axes[2].set_title("Score vs Comments")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()
