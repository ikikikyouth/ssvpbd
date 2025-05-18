import pandas as pd
import os
import re
from collections import Counter

category_files = [
    "stepsister_category.xlsx", "stepbrother_category.xlsx", "stepfather_category.xlsx",
    "stepmother_category.xlsx", "stepsiblings_category.xlsx", "stepfamily_category.xlsx",
    "stepson_category.xlsx", "stepdaughter_category.xlsx", "stepcousin_category.xlsx",
    "undefined_other_step_category.xlsx", "stepniece_category.xlsx", "stepnephew_category.xlsx",
    "stepaunt_category.xlsx", "stepuncle_category.xlsx", "stepgrandmother_category.xlsx",
    "stepgrandfather_category.xlsx", "stepgranddaughter_category.xlsx", "stepgrandson_category.xlsx"
]

def tokenize(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

for file in category_files:
    if os.path.exists(file):
        df = pd.read_excel(file)
        if "Title" in df.columns:
            all_words = []
            for title in df["Title"].dropna():
                all_words.extend(tokenize(str(title)))

            word_counts = Counter(all_words)
            
            word_freq_df = pd.DataFrame(word_counts.items(), columns=["Word", "Count"])
            word_freq_df = word_freq_df.sort_values(by="Count", ascending=False)
            
            output_file = file.replace(".xlsx", "_wordfrequency.xlsx")
            word_freq_df.to_excel(output_file, index=False)

print("doneeeee")
