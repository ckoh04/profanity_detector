import pandas as pd

read_file = pd.read_csv(r'unique_word_list.txt')
read_file.to_csv(r'unique_word_list.csv', index=False)

def load_profanity():
    profanity_list = []
    profanity_file = open('unique_word_list.csv', 'r', encoding="utf8")

    for word in profanity_file:
        profanity_list.append(word.strip().replace(',', ""))

    return profanity_list


profanities = load_profanity()
profanities = set(profanities)
print(profanities)







