import tweepy
from twilio.rest import Client

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Twilio API credentials
twilio_account_sid = "YOUR_TWILIO_ACCOUNT_SID"
twilio_auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_phone_number = "YOUR_TWILIO_PHONE_NUMBER"
recipient_phone_number = "YOUR_RECIPIENT_PHONE_NUMBER"

# Twitter account to monitor
target_twitter_account = "TARGET_TWITTER_ACCOUNT"

# Initialize the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize the Twilio client
client = Client(twilio_account_sid, twilio_auth_token)

# Monitoring and texting function
def monitor_tweets():
    tweets = api.user_timeline(screen_name=target_twitter_account, count=10)  # Adjust the count as per your needs
    for tweet in tweets:
        if "FREE3S" in tweet.text:
            code = extract_code(tweet.text)  # Implement your code extraction logic
            send_text_message(code)

# Function to send a text message
def send_text_message(code):
    message = client.messages.create(
        body=f"Congratulations! You won with code: {code}",
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"Text message sent. Message ID: {message.sid}")

# Function to extract the code from a tweet
def extract_code(tweet_text):
    # Implement your code extraction logic here
    return tweet_text.split("FREE3S")[0].strip()

# Run the monitoring function
monitor_tweets()