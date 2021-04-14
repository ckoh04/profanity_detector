import pandas as pd
import numpy
import sqlite3

read_file = pd.read_csv(r'unique_word_list.txt')
read_file.to_csv(r'unique_word_list.csv', index=False)

def load_profanity():
    profanity_list = []
    profanity_file = open('unique_word_list.csv', 'r', encoding="utf8")

    for word in profanity_file:
        profanity_list.append(word.strip().replace(',', ""))

    return profanity_list

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





