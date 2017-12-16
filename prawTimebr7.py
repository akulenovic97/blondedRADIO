import praw
import requests
import datetime

def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

r = praw.Reddit(client_id='SDNLVa0_tOJOfg' ,
                client_secret='-DIJH6XR_IJSC-VWdGqpiHq_088',
                username='frankeve',
                password='zalmina97',
                user_agent='blondedscrap by /u/frankeve')

subreddit = r.subreddit('FrankOcean')

hot_FO = subreddit.hot(limit=5)
for submission in hot_FO:
    print(submission)


FO_sub = r.submission(id='6xu91f')
print(type(get_date(FO_sub)))
