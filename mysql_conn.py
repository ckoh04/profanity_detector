import pymysql


def conn(self):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='chan102911130402',
                                 db='',
                                 charset='utf8')
    return conn
