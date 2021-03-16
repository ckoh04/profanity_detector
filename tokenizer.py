import spacy
import crawler
import nltk
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2500000
stop_words = spacy.lang.en.stop_words.STOP_WORDS

def tokenizer():

    text_chunk = open('data.csv', encoding="utf8").read()
    new_chunk = crawler.data_text_cleaning(text_chunk)
    nlp_text = nlp(new_chunk)

    with open('./tokenized_data.csv', 'w', encoding='utf-8') as f:
        for word in nlp_text:
            f.write(word.text + " " + word.pos_ + "\n")

if __name__ == "__main__":
    tokenizer()