from xvideos import XVideos
import csv
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

xvideos = XVideos()
video_links = []
predefined_start_of_url = "https://www.xvideos.com"

with open('january2015_scraperis.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        video_link = row[2]
        full_video_link = predefined_start_of_url + video_link
        video_links.append(full_video_link)

video_details_list = []

def fetch_video_details(video_url):
    details = xvideos.details(video_url)
    return {
        "Title": details['pavadinimas'],
        "Views": details['perziuros'],
        "URL": details['url'],
        "Like%": details['likesprocentas'],
        "Dislike%": details['dislikesprocentas'],
        "CommentCount": details['komentarucount']
    }

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(fetch_video_details, url): url for url in video_links}
    
    for future in tqdm(as_completed(futures), total=len(video_links), desc="Processing videos"):
        try:
            video_details = future.result()
            video_details_list.append(video_details)
        except Exception as e:
            print(f"nepavyko su url {futures[future]}: {e}")

df = pd.DataFrame(video_details_list)
df.to_excel('2015mar.xlsx', index=False)

print("done 'january2015_pavadinimai.xlsx'")
