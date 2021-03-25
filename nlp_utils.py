import spacy
import re
import nltk
import en_core_web_sm
# nlp = en_core_web_sm.load()
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import sent_tokenize
from bs4 import BeautifulSoup

#nltk.download('punkt')
#nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2500000
stop_words = spacy.lang.en.stop_words.STOP_WORDS
lemmatizer = WordNetLemmatizer()

contractions = {"aren't" : "are not", "can't" : "cannot", "couldn't": "could not",
                "didn't" : "did not", "doesn't" : "does not", "don't" : "do not", "hadn't" : "had not",
                "hasn't" : "has not", "haven't" : "have not", "he'd" : "he would", "he'll" : "he will",
                "he's" : "he is", "i'd" : "I would", "i'd" : "I had", "i'll" : "I will",
                "i'm" : "I am", "isn't" : "is not", "it's" : "it is", "it'll":"it will",
                "i've" : "I have", "let's" : "let us", "mightn't" : "might not",
                "mustn't" : "must not", "shan't" : "shall not", "she'd" : "she would", "she'll" : "she will",
                "she's" : "she is", "shouldn't" : "should not", "that's" : "that is", "there's" : "there is",
                "they'd" : "they would", "they'll" : "they will", "they're" : "they are", "they've" : "they have",
                "we'd" : "we would", "we're" : "we are", "weren't" : "were not", "we've" : "we have", "what'll" : "what will",
                "what're" : "what are", "what's" : "what is", "what've" : "what have", "where's" : "where is", "who'd" : "who would",
                "who'll" : "who will", "who're" : "who are", "who's" : "who is", "who've" : "who have", "won't" : "will not",
                "wouldn't" : "would not", "you'd" : "you would", "you'll" : "you will", "you're" : "you are", "you've" : "you have",
                "'re": " are","wasn't": "was not", "we'll":" will", "didn't": "did not"
}

def data_text_cleaning(data):
    # mention in write up that I am removing single letters since it is hard to decide either if it is text-in-speech or \n/etc.
    # escape characters (python mechanism [regex] to remove escape characters from text)

    data = re.sub('[^a-zA-Z0-9]', ' ', data)

    # remove newlines
    data = re.sub('\\n', '', data)

    # remove ip address (if exists)
    data = re.sub('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '', data)

    


    no_capitals = data.lower().split()
    stops = set(stopwords.words('english'))
    no_stops = [word for word in no_capitals if not word in stops]

    stemmer = nltk.stem.SnowballStemmer('english')
    stemmer_words = [stemmer.stem(word) for word in no_stops]

    return ' '.join(stemmer_words)

def tokenizer():

    text_chunk = open('data.csv', encoding="utf8").read()
    new_chunk = data_text_cleaning(text_chunk)
    nlp_text = nlp(new_chunk)
    print(nlp_text)
    #sentences = sent_tokenize(nlp_text)
    #print(sentences[0])

    #with open('./tokenized_data.csv', 'w', encoding='utf-8') as f:
    #    for word in nlp_text:
    #        f.write(word.text + " " + word.pos_ + " " + word.dep  "\n")
# def token_is_profane()

if __name__ == "__main__":
    tokenizer()