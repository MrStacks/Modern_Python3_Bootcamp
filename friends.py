import sqlite3
# If we had an existing database we could connect to it.
# But, since we don't, we can create our new database file through Python
connection = sqlite3.connect("my_friends.db")




connection.close() #close the connection at the end of script