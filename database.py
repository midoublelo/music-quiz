import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE quiz(username text, password text, score integer)")
    con.commit()
con = sql_connection()
sql_table(con)

cursorObj = con.cursor()
cursorObj.execute("INSERT INTO quiz VALUES('millo', 'pass', 7)")
con.commit()