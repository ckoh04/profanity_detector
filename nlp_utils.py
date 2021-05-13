import spacy
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import TweetTokenizer
from nltk import sent_tokenize
from emoji import demojize
#nltk.download('wordnet')
#nltk.download('punkt')
#nltk.download('stopwords')
#0-nltk.download('averaged_perceptron_tagger')
nlp = spacy.load('en_core_web_sm')
nlp.max_length = 2500000
stop_words = spacy.lang.en.stop_words.STOP_WORDS
lemmatizer = WordNetLemmatizer()
tokenizer = TweetTokenizer()
stops = set(stopwords.words('english'))




def data_text_cleaning(data):
    data = data.lower()

    # emojis to characters
    data = demojize(data)

    data = re.sub('\n\n', '', data)
    data = data.rstrip("\r")
    data = data.rstrip("\n")
    data = data.rstrip("\n\n")
    data = data.rstrip("\r\n")
    data = data.rstrip("\t")
    data = data.strip()
    # remove newlines
    data = re.sub('\\n', '', data)
    data = re.sub(r'(\r\n.?)+', r'\r\n', data)
    data = re.sub('[^a-zA-Z0-9]', ' ', data)
    # remove ip address (if exists)
    data = re.sub('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '', data)
    #data = tokenizer.tokenize(data)
    data = sent_tokenize(data)
    data = [lemmatizer.lemmatize(word, 'v') for word in data]
    no_stops = [word for word in data if not word in stops]

    return ' '.join(no_stops)

def clean_profane_wordlist():
    word_list = open('profanities.txt', encoding="utf8").read()
    cleaned_word_list = re.sub('[,"]', '', word_list)

    with open('./word_list.txt', 'w', encoding="utf=8") as file:
        file.write(cleaned_word_list + "\n")

def remove_duplicate():
    word_list = open('word_list.txt', encoding="utf8").read()

    unique_cleaned_word_list = (list(set(nltk.word_tokenize(word_list))))

    with open('./unique_word_list.txt', 'w', encoding='utf=8') as file:
        for word in unique_cleaned_word_list:
            file.write(word + ',\n')

def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatize_sentence(data):
    nltk_tagged = nltk.pos_tag(data)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

if __name__ == "__main__":
    reddit_data = open('data.csv', encoding="utf8").read()

    profanity_list = open('profanities.txt', encoding="utf8").read()
    data_to_save = (data_text_cleaning(reddit_data))
    print((data_text_cleaning(reddit_data)))
    with open('./cleaned_data.txt', "w", encoding="utf8") as file:
        file.write(data_to_save)



