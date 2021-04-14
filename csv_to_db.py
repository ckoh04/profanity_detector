import sqlite3
import pandas as pd
from pandas import DataFrame
import csv

import sys
'''

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("DROP TABLE reddit")
cur.execute("CREATE TABLE IF NOT EXISTS reddit (date, title, body, comment_body);")


with open("data.csv", 'r', encoding="utf8") as file:
    reader = csv.DictReader(file)
    to_db = [(i['date'], i['title'], i['body'], i['comment_body']) for i in reader]


cur.executemany("INSERT INTO reddit (date, title, body, comment_body) VALUES (?,?,?,?);", to_db)
con.commit
con.close()
'''
def make_data_db():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("DROP TABLE reddit")
    cur.execute("CREATE TABLE IF NOT EXISTS reddit (id INTEGER PRIMARY KEY AUTOINCREMENT, date, title, body, comment_body, profanity INTEGER DEFAULT 0);")
    pd.read_csv("data.csv").to_sql("reddit", con, if_exists='append', index=False)
    con.close()



'''
def make_commentfocused_db():
    comments = csv.reader(open("comments.csv", encoding="utf8"))
    next(comments)
    con = sqlite3.connect("specific_data.db")
    # con.execute("DROP TABLE comments")
    con.execute("CREATE TABLE IF NOT EXISTS specificdata(id INTEGER PRIMARY KEY AUTOINCREMENT, comment_id, comment, is_profanity INTEGER DEFAULT 0)")
    cur = con.cursor()

    con.executemany("INSERT INTO specificdata(id, comment_id, date, title, comment) VALUES (?, ?)",
                    ((rec[0], rec[4]) for rec in comments))
    con.execute("DELETE FROM specificdata WHERE comment IS NULL OR trim(comment) = '';")
    con.commit()

def make_tokenized_commentfocused_db():
    comments = csv.reader(open("comments_tokenized.db.csv", encoding="utf8"))
    next(comments)
    con = sqlite3.connect("tokenized_specificdata.db")
    # con.execute("DROP TABLE comments")
    con.execute("CREATE TABLE IF NOT EXISTS tokspecificdata(id INTEGER PRIMARY KEY AUTOINCREMENT, comment_id, comment, is_profanity INTEGER DEFAULT 0)")
    cur = con.cursor()

    con.executemany("INSERT INTO tokspecificdata(comment_id, comment) VALUES (?, ?)",
                    ((rec[0], rec[4]) for rec in comments))
    con.execute("DELETE FROM tokspecificdata WHERE comment IS NULL OR trim(comment) = '';")
    con.commit()
'''



def make_comment_db():

    comments = csv.reader(open("comments.csv", encoding="utf8"))
    next(comments)
    con = sqlite3.connect("comments.db")
    con.execute("DROP TABLE comments")
    con.execute("CREATE TABLE IF NOT EXISTS comments(comment_id, comment, is_profanity)")
    cur = con.cursor()

    con.executemany("INSERT INTO comments(comment_id, comment, is_profanity) VALUES (?, ?, ?)", ((rec[0], rec[4], rec[5]) for rec in comments))
    con.execute("DELETE FROM comments WHERE comment IS NULL OR trim(comment) = '';")
    con.commit()
    con.close()


def make_tok_comment_db():

    tokenized_comments = csv.reader(open("comments_tokenized.csv", encoding="utf8"))
    next(tokenized_comments)
    con = sqlite3.connect("comments_tokenized.db")
    con.execute("DROP TABLE tok_comments")
    con.execute("CREATE TABLE IF NOT EXISTS tok_comments(comment_id, comment, is_profanity)")
    cur = con.cursor()

    con.executemany("INSERT INTO tok_comments(comment_id, comment, is_profanity) VALUES (?, ?, ?)", ((rec[0], rec[4], rec[5]) for rec in tokenized_comments))
    con.execute("DELETE FROM tok_comments WHERE comment IS NULL OR trim(comment) = '';")
    con.commit()
    con.close()

# make_data_db()
make_tok_comment_db()
#make_comment_db()
