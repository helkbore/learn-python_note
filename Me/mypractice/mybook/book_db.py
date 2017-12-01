#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'数据库操作 2017年12月1日'

import sqlite3



def save_dict(table, d):
    conn = sqlite3.connect('E:\\备份\\sqlite\\kindlebook.db')
    cursor = conn.cursor()
    cols = ', '.join(d.keys())
    qmarks = ', '.join(['%s'] * len(d))
    sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, cols, qmarks)
    print(sql)
    # print(qmarks)
    # cursor.execute(sql)
    cursor.close()
    print("book_db.save_book")

save_dict('abc', {'a': 'aa', 'b': 'bb'})
