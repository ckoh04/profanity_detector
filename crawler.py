import praw
import reddit_info
import csv
import time
from datetime import datetime


CLIENT_ID = reddit_info.Reddit.client_id
CLIENT_SECRET = reddit_info.Reddit.secret
USER_AGENT = 'Chrome'
SUB_REDDIT = 'CoronaVirusInfo'
LIMIT = 999
def scrape_reddit():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent=USER_AGENT)
    print("=================================")
    print("Scraping Reddit Submission")
    print("---------------------------------\n\n")

    scrape_data = []
    total_subreddit = 0


    for submission in reddit.subreddit(SUB_REDDIT).hot(limit=LIMIT):
        total_subreddit += 1
        submission_dict = vars(submission)

        # Title
        print("[Title %03d] : " % (total_subreddit), submission.title)
        writelist = [datetime.utcfromtimestamp(submission.created_utc),
                     submission.title,
                     submission_dict['selftext'].rstrip("\n"), 0]

        # Comment
        post = reddit.submission(id=submission_dict['id'])
        total_comment = 0
        for top_level_comment in post.comments:
            writelist.append(top_level_comment.body.strip("\n"))
            total_comment += 1

        writelist[3] = total_comment
        scrape_data.append(writelist)
        print("-----------------------------------------")

    return scrape_data, total_subreddit

def write_csv(scrape_data, total_subreddit):
    with open(time.strftime("data_%Y%m%d.csv", time.localtime()),
              'wt', encoding='utf=8') as file:
         writer = csv.writer(file, delimiter=",", lineterminator="\n")

         for data in scrape_data:
             writer.writerow(data)


def crawler():
    scrape_data, total_subreddit = scrape_reddit()
    write_csv(scrape_data, total_subreddit)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    crawler()

