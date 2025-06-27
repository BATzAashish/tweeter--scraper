from scraper.twitter_api import fetch_tweets
from scraper.save import save_tweets_to_csv

if __name__ == "__main__":
    username = "sebastianroehl"  # <-- Replace with the desired Twitter username
    tweet_count = 10        # <-- Change if you want a different number of tweets

    tweets = fetch_tweets(username, tweet_count)
    save_tweets_to_csv(tweets, f"data/{username}_tweets.csv")
    print(f"Saved {len(tweets)} tweets to data/{username}_tweets.csv")