import pandas as pd
import re
from wordfreq import word_frequency

file_path = "20152024overall.xlsx"
df = pd.read_excel(file_path)

def has_english_word(title, threshold=1e-6):  
    title_words = re.findall(r'\b[a-zA-Z]+\b', title)
    return any(word_frequency(word.lower(), 'en') > threshold for word in title_words) if title_words else False

def clean_titles(df):
    df["Title"] = df["Title"].astype(str).str.strip()
    df = df[df["Title"].apply(has_english_word)]
    df = df[~df["Title"].str.match(r'^\d+$')]
    df = df[df["Title"].str.count(r'\b\w+\b') > 1]
    df = df.drop_duplicates(subset=["Title"])
    return df

df_cleaned = clean_titles(df)

df_cleaned.to_excel("20152024overall_cleaned.xlsx", index=False)

print("done")
