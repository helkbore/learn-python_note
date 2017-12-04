#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'数据库操作 2017年12月1日'

import sqlite3



def save_book(table, d):
    conn = sqlite3.connect('E:\\备份\\sqlite\\kindlebook.db')
    cursor = conn.cursor()

    # -- 构建select 语句
    sql = "select id from %s where book_name = '%s' and ext = '%s' " % (table, d['book_name'], d['ext'])
    # print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    # print()
    if len(result) == 0:



        # --构造insert sql语句
        cols = ','.join(d.keys())
        # ----将list中的其他类型转换位str
        dvalue = list(d.values())
        for s in dvalue:
            dindex = dvalue.index(s)
            dvalue[dindex] = str(s).strip()

        values = "','".join(dvalue)
        values = "'" + values + "'"

        sql = "insert into %s ( %s ) values ( %s )" % (table, cols, values)
        # print(sql)



        cursor.execute(sql)
        # print(cursor.rowcount)
        cursor.close()
        # print("-- book_db.save_book")
        conn.commit()
        conn.close()


# d = {'book_name': 'test', 'size': '100', 'ext': 'mobi', 'origin_name': 'test.mobi'}
# table = 'book'
# # save_dict('book', book)
# sql = "select id from %s where book_name = '%s' and ext = '%s' " % (table, d['book_name'], d['ext'])
# print(sql)