import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from wordcloud import WordCloud
from sqlalchemy import create_engine

con = sqlite3.connect("sorted_comments.db")
data = pd.read_sql('SELECT * FROM comments', con)

con2 = sqlite3.connect("sorted_tokenized_comments.db")
tokenized_data = pd.read_sql("SELECT * FROM tok_comments", con2)


#data.head()
print(type(data))
for col in data.columns:
    print(col)

print(data.shape)
# print(data.head())
is_profanity = data["is_profanity"]
is_profanity.value_counts().plot(kind='bar')
plt.show()

data_length = (data["comment"]).apply(len)
print(data_length.head())
plt.figure(figsize= (12,5))
plt.hist(data_length, bins=50, alpha=0.5, color="b", label="word_length")
plt.yscale('log')
plt.legend
plt.show()
print("Smallest Length: ", np.min(data_length))
print("Biggest Length: ", np.max(data_length))
print("Average Length: ", np.mean(data_length))

word_cloud = WordCloud(width = 800, height = 600, font_path = 'arial.ttf', background_color= 'white').generate(" ".join(tokenized_data['comment']))
plt.figure(figsize=(20, 15))
plt.imshow(word_cloud)
plt.show()

con.close()
con2.close()