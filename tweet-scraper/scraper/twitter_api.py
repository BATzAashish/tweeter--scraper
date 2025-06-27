import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

def fetch_tweets(username, count=10):
    # Get user ID from username
    user = client.get_user(username=username)
    user_id = user.data.id
    tweets = client.get_users_tweets(id=user_id, max_results=min(count, 100), tweet_fields=["created_at","text"])
    tweet_data = []
    if tweets.data:
        for tweet in tweets.data:
            tweet_data.append({
                "created_at": tweet.created_at,
                "text": tweet.text
            })
    return tweet_data