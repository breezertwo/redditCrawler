# redditCrawler

Crawler for reddit memes

## Features

- add desired subreddits to crawler
- set amount of memes per sub
- dosen't store duplicate entries
- only stores direct image links (no slideshows, videos)
- schedule job to crawl top memes every day

## Requirements

- [schedule] - Python job scheduling for humans
- [PRAW] - Python Reddit API Wrapper
- [pymongo] - a native Python driver for MongoDB

## How to use

- Add your credentials for reddit to the config.json (create an app [here])
- Change your database in the .py script at the comment (posts will be stored at collection "redditPosts")

Add or remove subreddits here:

```python
subs = ['trippinthroughtime', 'funny', 'memes']
```

Add or remove extensions here:

```python
extensions = ['.jpg', '.png', '.gif']
```

Change this line to choose between r/hot, r/top... and the amount of posts you want to get:

```python
topPosts = reddit.subreddit(sub).top(limit=15)
```

Change this line to create a schedule at which times the crawler should be executed:

```python
schedule.every().day.at("09:00").do(crawlAllSubs)
```

[//]: # "Links"
[schedule]: https://schedule.readthedocs.io/en/stable/
[praw]: https://praw.readthedocs.io/en/latest/
[pymongo]: https://github.com/mongodb/mongo-python-driver
[here]: https://www.reddit.com/prefs/apps/
