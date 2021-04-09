import sqlite3
import nlp_utils

#-----------------------------------------------------------#
untokenized_db = 'data.db'
conn = sqlite3.connect(untokenized_db)
cur = conn.cursor()

#-----------------------------------------------------------#
tokenized_db = 'tokenized_data.db'
conn2 = sqlite3.connect(tokenized_db)
cur2 = conn2.cursor()
cur2.execute("DROP TABLE comment_token")
cur2.execute("CREATE TABLE IF NOT EXISTS comment_token (id INTEGER PRIMARY KEY AUTOINCREMENT, comment, is_profanity INTEGER DEFAULT 0);")
conn2.commit()


#-----------------------------------------------------------#

cur.execute("SELECT comment_body AS comment FROM reddit;")

rows = cur.fetchall()

def main():
    for row in rows:
        for section in row:
            nlp_comments = nlp_utils.data_text_cleaning(section)
            #print(nlp_comments)

    cur2.executemany("INSERT INTO comment_token (comment) VALUES (?)", nlp_comments)
    conn2.commit()



main()
