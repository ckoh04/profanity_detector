from keras.models import load_model
from keras.preprocessing import sequence
import pickle

string = ['well i am pretty sure they said fuck you to russia a few times and germany at least once']

string_tok = tok.texts_to_sequences(string)

string_tok = sequence.pad_sequences(string_tok, maxlen=200)

pre = model.predict(string_tok)

for i in pre:
    if i > 0.5:
        print("profane")
    else:
        print("not profane")
