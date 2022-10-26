import sqlite3

# DB-API spec for talking to relational databases in Python

connection = sqlite3.connect("shopping_list.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table list")
except:
    pass

cursor.execute("create table list (id integer primary key, description text)")

cursor.execute("insert into list (description) values ('Avocado')")
cursor.execute("insert into list (description) values ('Cucumbers')")
cursor.execute("insert into list (description) values ('Greens')")
cursor.execute("insert into list (description) values ('Mushrooms')")
cursor.execute("insert into list (description) values ('Spinach')")

connection.commit()
connection.close()

print("done.")
