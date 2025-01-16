import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("insert into user (name) values ('HRB');")

cur.execute("insert into user (name) values ('Hiran Ram Babu');")

connection.commit()
connection.close()