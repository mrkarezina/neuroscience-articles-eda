import pandas as pd
import json

json_file = "neuroscience.json"
save_file = "neuroscience_articles.csv"

with open(json_file) as f:
    json_data = json.load(f)

# Merge the meta data (string) with main data
merged = []
for article in json_data:
    meta = json.loads(article["meta_data"])
    del article["meta_data"]

    merged.append({**article, **meta})

df = pd.DataFrame(merged)
df = df.drop(['viewport', 'og', 'frontiers', 'fb', 'Keywords'], 1)

df = df.mask(df.applymap(str).eq('{}'))

print(df.shape)

df.to_csv(save_file)
