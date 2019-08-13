#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('master.db',check_same_thread=False)
cursor=connection.cursor()

cursor.execute('''
            CREATE TABLE log(
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                time VARCHAR(64),
                ticker VARCHAR(64),
                price INTEGER,
                stop_loss INTEGER,
                volume INTEGER,
                buy_sell VARCHAR(64)
            )
            '''
            )

connection.commit()

cursor.close()
connection.close()
