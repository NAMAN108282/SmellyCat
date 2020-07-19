#Import modules for the 
from datetime import timedelta, datetime
from dateutil import parser
from time import sleep
import requests
import feedparser

#Create a Bot using Botfather to get TELEGRAM API TOKEN
#Create a channel and set it's  new id for CHANNEL ID
#Add Bot to the channel as an Admin

BOT_TOKEN ='' # REPLACE WITH YOUR BOT'S TELEGRAM API TOKEN
CHANNEL_ID =' ' #REPLACE WITH CHANNEL ID OF CHANNELNAME AS @channel_id

REDDIT_RSSFEED_URL = 'https://www.reddit.com/r/worldnews/top.rss?t=day&limit=30'


def send_updates(message):
    requests.get(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&text={message}')


def main():
    send_updates("News Update of the Day:")
    rss_new_feed = feedparser.parse(REDDIT_RSSFEED_URL) #RSS FEED URL Pattern: https://www.reddit.com/r/<subreddit>/t>
    for entry in rss_new_feed.entries:
        parsed_date = parser.parse(entry.updated)
        send_updates(entry.links[0].href)



if __name__ == "__main__":
    while(True):
        main()
        sleep(20*60)


