import sqlite3
# If we had an existing database we could connect to it.
# But, since we don't, we can create our new database file through Python
connection = sqlite3.connect("my_friends.db") # & next time code runs it will connect to this database
# create cursor object
c = connection.cursor()
# execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, close INTEGER);")
insert_query = '''INSERT INTO friends 
                    VALUES ('Merriwether', 'Lewis', 7)'''
c.execute(insert_query)
#commit changes
connection.commit()
connection.close() #close the connection at the end of script