'''Video 377 - SQL Injection!
'''
import sqlite3

connection = sqlite3.connect("users.db")
# create cursor object
c = connection.cursor()


# commit changes
connection.commit()

# the above commands look the same as what we have seen
# in this case we'll get something back, however
connection.close()