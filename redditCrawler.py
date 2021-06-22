import time
import json
import schedule
import praw
from pymongo import MongoClient

with open("config.json") as jsonConfig:
    config = json.load(jsonConfig)

dbClient = MongoClient(config['mongoDB']['baseUrl'])
# change xxx to database name
db=dbClient.xxx 
reddit = praw.Reddit(client_id=config['redditAPI']['client_id'], client_secret=config['redditAPI']['client_secret'], user_agent=config['redditAPI']['user_agent'])

subs = ['trippinthroughtime', 'funny', 'memes']
extensions = ['.jpg', '.png', '.gif']

def crawlSub(sub):
    i = 0
    topPosts = reddit.subreddit(sub).top(limit=15)
    for post in topPosts:
        if post.url.endswith(tuple(extensions)):
          postObj = {
            'title' : post.title,
            'url' : post.url,
            'sub' : sub
          }
          if db.redditPosts.count_documents({ 'url': post.url }, limit = 1) != 1:
            db.redditPosts.insert_one(postObj)
            i += 1
    print('[RC] Added {} new posts to db for sub {}'.format(i , sub))

def crawlAllSubs():
    print('[RC] Starting crawl...')
    for sub in subs:
        crawlSub(sub)
    print('[RC] Crawl finsihed...')

schedule.every().day.at("09:00").do(crawlAllSubs)

print('[S] Starting schedule...')
while 1:
    schedule.run_pending()
    time.sleep(1)