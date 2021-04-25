import pandas as pd
import numpy
from collections.abc import Iterable
import sqlite3


pd.set_option('display.max_rows', 100)
read_file = pd.read_csv(r'unique_word_list.csv')
# read_file.to_csv(r'unique_word_list.csv', index=False)
df = pd.read_csv("comments.csv")
tokenized_df = pd.read_csv("comments_tokenized.csv")

def load_profanity():
    profanity_list = []
    profanity_file = open('unique_word_list.csv', 'r', encoding="utf8")

    for word in profanity_file:
        profanity_list.append(word.strip().replace(',', ""))

    return profanity_list

profanity = load_profanity()
print(profanity)
# print(df.columns)


# df.loc[df['comment_body'].apply(lambda x: any([k in x for k in profanity])), 'is_profanity'] = 1
# print(df.head())
# df.to_csv("sorted_comments.csv")

tokenized_df.loc[df['comment_body'].apply(lambda x: any([k in x for k in profanity])), 'is_profanity'] = "yes"
tokenized_df.to_csv("sorted_tokenized_comments.csv")
#print(df.head())



'''
def check_commentdb(profanities):
    df = pd.read_csv("")

    print("to be implemented")


def check_tokenizedcommentdb(profanities):
    df = pd.read_csv("tokenized_data.csv")
    print(df.loc[:, ['comment_body']])
    # df.loc[df['comment_body'].str.contains(pattern), 'is_profanity'] = 1
    print("to be implemented")


def check_profanity():
    
    profanities = load_profanity()
    profanities = set(profanities)
    #print(type(profanities))
    check_tokenizedcommentdb(profanities)

check_profanity()

'''


