import spacy

nlp = spacy.load('en_core_web_sm')

def tokenizer():
    text_chunk = open('data_20210303.csv', encoding="utf8").read()
    nlp_text = nlp(text_chunk)

    for word in nlp_text:
        print(word.text)

    # with open(file, 'w', encoding='utf-8') as f:
    #     for word in f:
    #         sp(word)
    #         print(word.text, word.pos_)
    #

if __name__ == "__main__":
    tokenizer()