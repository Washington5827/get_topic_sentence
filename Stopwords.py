import re
import sqlite3


def db_creat_Stopwords():
    '''创建表Stopwords'''
    db = sqlite3.connect("PythonLP.db")
    cur = db.cursor()

    sql = '''CREATE TABLE Stopwords(WORD CHAR(50) PRIMARY KEY NOT NULL);'''
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def db_insert_Stopwords(word):
    '''向表Stopwords中压入数据'''
    db = sqlite3.connect("PythonLP.db")
    cur = db.cursor()

    # 新增
    sql = 'INSERT INTO Stopwords(WORD) VALUES("%s");' % (word)
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def db_init_Stopwords():
    '''从txt文件初始化表Stopwords'''
    fopen = open("stopwords.txt", "r")
    contents = fopen.read()

    # 将单词间均替换为空格
    stopwords = re.sub("[\.,\?]\n", " ", contents)
    # 把单词拉入到stopwords列表中
    stopwords = re.findall("\w*'?\w+", stopwords, re.S)

    # 将list转为set
    s = set(stopwords)
    # 压入数据
    for item in s:
        db_insert_Stopwords(item)


def db_search_Stopwords(word):
    '''在表Stopwords中寻找指定词汇'''
    db = sqlite3.connect("PythonLP.db")
    cur = db.cursor()

    # 新增
    sql = 'SELECT*FROM Stopwords WHERE WORD LIKE "%s";' % (word)
    cur.execute(sql)
    result = cur.fetchone()
    return result


def remove_stopwords_from_words(list):
    '''从指定list中删除stopword'''
    # 创建空集合
    recurred = set()
    # 发现其中的stopword
    for word in list:
        if type(db_search_Stopwords(word)) == type(()):
            recurred.add(word)
    # 删除s中所有的stopword
    for item in recurred:
        list.remove(item)
        #print("%s removed" % item)


def init_Stopwords():
    db_creat_Stopwords()
    db_init_Stopwords()
