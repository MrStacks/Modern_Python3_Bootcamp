import sqlite3

connection = sqlite3.connect("my_friends.db")
# create cursor object
c = connection.cursor()
# let's say I want to SELECT * every friend in the db
c.execute("SELECT * FROM friends")

# commit changes
connection.commit()

# the above commands look the same as what we have seen
# in this case we'll get something back, however

connection.close()