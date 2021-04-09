import spacy
import pandas as pd
import csv, sqlite3
import nlp_utils
import re
import emoji
import nltk
import en_core_web_sm
# nlp = en_core_web_sm.load()
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk import sent_tokenize
from emoji import demojize
from bs4 import BeautifulSoup
from collections import Counter

#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2500000

df = pd.read_csv("data.csv")
df.drop(columns="date")
comment = df.loc[0, "comment_body"]

df["comment_body"] = df["comment_body"].apply(lambda x: [nlp_utils.data_text_cleaning(sent.text) for sent in nlp(x).sents])
df = df.explode("comment_body", ignore_index=True)

df.index.name = "comment_id"
df.head()

df.to_csv("comments_tokenized.csv")

