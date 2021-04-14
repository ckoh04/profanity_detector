import spacy
import pandas as pd
import nlp_utils
import spacy
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer

#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('stopwords')
stop_words = spacy.lang.en.stop_words.STOP_WORDS
lemmatizer = WordNetLemmatizer()
tokenizer = TweetTokenizer()
stops = set(stopwords.words('english'))
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2500000

def create_comment_csv():
    df = pd.read_csv("data.csv")
    df.drop(columns="date")
    comment = df.loc[0, "comment_body"]

    df["comment_body"] = df["comment_body"].apply(lambda x: [sent.text for sent in nlp(x).sents])
    df = df.explode("comment_body", ignore_index=True)

    df.index.name = "comment_id"
    df.head()
    df["is_profanity"] = 0

    df.to_csv("comments.csv")




def create_tokenized_comment_csv():
    df = pd.read_csv("data.csv")
    df.drop(columns="date")
    comment = df.loc[0, "comment_body"]

    df["comment_body"] = df["comment_body"].apply(lambda x: [nlp_utils.data_text_cleaning(sent.text) for sent in nlp(x).sents])
    df = df.explode("comment_body", ignore_index=True)
    df.index.name = "comment_id"

    df.head()
    df["is_profanity"] = 0

    df.to_csv("comments_tokenized.csv")

#create_comment_csv()
create_tokenized_comment_csv()


