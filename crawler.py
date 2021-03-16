import nltk
import praw
import reddit_info
from bs4 import BeautifulSoup
import re
import csv
import time
from datetime import datetime
from praw.models import MoreComments
import mysql_conn
import mariadb
import sys
import json
import pandas as pd
from nltk.corpus import stopwords
from pandas import DataFrame
pd.set_option("display.max_rows", None, "display.max_columns", None)

CLIENT_ID = reddit_info.Reddit.client_id
CLIENT_SECRET = reddit_info.Reddit.secret
USER_AGENT = 'Chrome'
SUB_REDDIT = 'tifu+The_Donald+worldnews+gonewild+nottheonion'
LIMIT = 9999


def scrape_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    print("=================================")
    print("Scraping Reddit Submission")
    print("---------------------------------\n\n")

    scrape_data = []
    headings = ["date", "title", "body", "comment_body"]
    scrape_data.append(headings)
    total_subreddit = 0
    for submission in reddit.subreddit(SUB_REDDIT).hot(limit=LIMIT):
        submission.comments.replace_more
        total_subreddit += 1
        submission_dict = vars(submission)

        # Title
        print("[Title %03d] : " % (total_subreddit), submission.title)
        writelist = [datetime.utcfromtimestamp(submission.created_utc),
                     submission.title,
                     submission_dict['selftext'].rstrip("\n\n\n")]

        # Comment
        post = reddit.submission(id=submission_dict['id'])
        # total_comment = 0
        comments = []
        for top_level_comment in post.comments.list():
            if isinstance(top_level_comment, MoreComments):
                continue
            # writelist.append(top_level_comment.body)
            # .body.strip("\n"))
            comments.append(top_level_comment.body.strip("\n"))
            #total_comment += 1
        writelist.append(comments)
        # writelist[3] = total_comment
        scrape_data.append(writelist)

        print("-----------------------------------------")

    return scrape_data, total_subreddit


def write_csv(scrape_data, total_subreddit):
    with open(time.strftime("data.csv", time.localtime()),
              'wt', encoding='utf=8') as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")

        for data in scrape_data:
            writer.writerow(data)

def data_text_cleaning(data):
    only_english = re.sub('[^a-zA-Z]', ' ', data)

    no_capitals = only_english.lower().split()

    stops = set(stopwords.words('english'))
    no_stops = [word for word in no_capitals if not word in stops]

    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer_words = [stemmer.stem(word) for word in no_stops]

    return ' '.join(stemmer_words)


def write_json(scrape_data, total_subreddit):
    with open(time.strftime("data.txt", time.localtime()), 'wt') as file:
        texts = []
        for _ in scrape_data:
            texts.append(json.loads(next(file).strip()))

def make_dataframe():
    data = pd.read_csv(r'data.csv')
    # for _ in data:

    df = pd.DataFrame(data, columns=['date', 'title', 'body', 'comment_body'])
    print(df)

def crawler():
    scrape_data, total_subreddit = scrape_reddit()
    write_csv(scrape_data, total_subreddit)
    make_dataframe()
    # write_json(scrape_data, total_subreddit)

#
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    crawler()
