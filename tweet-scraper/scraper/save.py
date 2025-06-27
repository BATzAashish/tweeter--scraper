import csv
import os

def save_tweets_to_csv(tweets, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["created_at", "text"])
        writer.writeheader()
        writer.writerows(tweets)