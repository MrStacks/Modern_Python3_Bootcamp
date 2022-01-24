import sqlite3

connection = sqlite3.connect("my_friends.db")
# create cursor object
c = connection.cursor()
# commit changes
connection.commit()
connection.close()