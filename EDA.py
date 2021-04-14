import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from wordcloud import WordCloud
from sqlalchemy import create_engine



def get_db_non_tok_data(conn):
    data = pd.read_sql_table('crw_data', conn)
    return data

def get_db_tok_data(conn):
    data = pd.read_sql_table('tokenized_data', conn)
    return data


data = get_db_non_tok_data(conn)
data_tok = get_db_tok_data(conn)


conn_server = mysql_conn_server()
data = get_db_non_tok_data(conn_server)
data_tok = get_db_tok_data(conn_server)


data.head()
print(type(data))

data.BOARD.value_counts().plot(kind='bar')

data.CATEGORY.value_counts().plot(kind='bar')
data.shape

data_length = (data['TITLE'] + " " + data['CONTENT']).apply(len)
data_length.head()


plt.figure(figsize=(12,5))
plt.hist(data_length, bins = 50, alpha=0.5, color = 'b', label='word_length')
plt.yscale('log')

plt.legend()
plt.show()

print("길이 최소 값 : ", np.min(data_length))
print("길이 최대 값 : ", np.max(data_length))
print("길이 평균 값 : ", np.mean(data_length))

data_tok.head()


cloud = WordCloud(width = 800, height = 600, font_path = 'arial.ttf', background_color= 'white').generate(" ".join(data_tok['CONTENT_TOK']))
plt.figure(figsize=(20, 15))
plt.imshow(cloud)
plt.show()