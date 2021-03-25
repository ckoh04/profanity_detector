import numpy as np, pandas as pd
import sys, os, re, csv, time, codecs

from nlp_utils import data_text_cleaning
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Activation, Input, LSTM, Embedding, Dropout, Dense
from keras.layers import GlobalMaxPool1D, Bidirectional
from keras.preprocessing.text import Tokenizer

from keras.models import Model
from keras import initializers, regularizers, constraints, optimizers, layers


start = time.time()

train = pd.read_csv('profanities.csv', encoding='latin-1')
submission = pd.read_csv('data.csv')

print('Reading the dataset...')

list_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
y = train[list_classes].values

list_sentences_train = train["comment_text"].apply(lambda comment: data_text_cleaning(comment))
