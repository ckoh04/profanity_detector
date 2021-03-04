import pandas as pd

def make_unique(data):
    data_list = data.iloc[:, 0].values
    data_list_after_preprocessing = list(set(data_list))
    nltk = []
    for word in data_list_after_preprocessing:
        word = word.strip()
        word = word + ",,,0,NNP,*,F," + word + ",*,*,*,*"
        nltk.append(word)

    with open('./post_duplication.csv', 'w', encoding='utf-8') as f:
        for word in nltk:
            f.write(word + "\n")

def get_user_dic():
    data_user_origin = pd.read_csv('./post_duplication.csv', header=None)
    data_user_add = pd.read_csv('./profanities.txt', header=None)
    data = pd.concat([data_user_origin, data_user_add], sort=True, axis = 0)
    return data

if __name__ == "__main__":
    data = get_user_dic()
    make_unique(data)