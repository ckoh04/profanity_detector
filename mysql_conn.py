import pymysql


def conn(self):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='',
                                 charset='utf8')
    return conn
