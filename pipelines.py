#! /home/endi/anaconda/bin/python2.7


import sqlite3 as sql


def process_item(item):

    # setup database
    conn = sql.connect('FTSE.db')
    cur = conn.cursor()


    # create table if not exist
    cur.execute("CREATE TABLE IF NOT EXISTS FTSE \
        (ID INTEGER, \
        Symbol TEXT, \
        Name TEXT, \
        Datetime TEXT, \
        Price REAL, \
        Change REAL, \
        Change_Rate REAL,\
        Volume INTEGER \
        )")


    # insert data into table
    for each_stock in item:
        cur.execute("INSERT INTO FTSE \
            (ID, \
            Symbol, \
            Name, \
            Datetime, \
            Price, \
            Change, \
            Change_Rate, \
            Volume \
            ) \
        VALUES(?,?,?,?,?,?,?,?)", \
        (\
            each_stock.ID, \
            each_stock.Symbol, \
            each_stock.Name, \
            each_stock.Datetime, \
            each_stock.Price, \
            each_stock.Change, \
            each_stock.Change_Rate, \
            each_stock.Volume \
        ))

    conn.commit()

    conn.close()