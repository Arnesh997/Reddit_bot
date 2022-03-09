from http import client
import praw
import re
import time

reddit = praw.Reddit(client_id='',
                     client_secret ='',
                     user_agent = '<console:reddit_bot:0.0.1 (by u/)>',
                     username = '',
                     password='')

subreddits=['bottestingself','bottestself2']
pos = 0 #Counter for array

title="First Try"
url="https://en.wikipedia.org/wiki/Honey#/media/File:Runny_hunny.jpg"

def post():
    global subreddits
    global pos
    
    try:
        subreddit = reddit.subreddit(subreddits[pos])
        subreddit.submit(title,url=url)
    
        pos=pos+1
    
        if (pos <= len(subreddits) - 1):
            post()
        else:
            print("Done")
    except praw.exceptions.APIException as e:
        print(e.message)
        
         
post()


    