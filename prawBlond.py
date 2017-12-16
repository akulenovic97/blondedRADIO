import praw
import datetime
import unicodedata

reddit = praw.Reddit(client_id='SDNLVa0_tOJOfg' ,
                     client_secret='-DIJH6XR_IJSC-VWdGqpiHq_088',
                     username='frankeve',
                     password='zalmina97',
                     user_agent='blondedscrap by /u/frankeve')

subreddit = reddit.subreddit('FrankOcean')

hot_python = subreddit.hot(limit=3)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.format(submission.title,
                                                                   submission.ups,
                                                                   submission.downs,
                                                                   submission.visited))
            


#WORKING WITH COMMENTS
comments = submission.comments.list()
#Doesn't include reply
for comment in comments:
    unicodedata.encode('comment','ignore')
    print(20*'-')
    print(comment.body)

def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

FO_date = get_date(hot_python)
unicodedata.encode('ascii', 'ignore')
print(FO_date)


    
