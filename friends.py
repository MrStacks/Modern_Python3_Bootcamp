import sqlite3
# If we had an existing database we could connect to it.
# But, since we don't, we can create our new database file through Python
connection = sqlite3.connect("my_friends.db") # & next time code runs it will connect to this database
# create cursor object
c = connection.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, close INTEGER);")
# insert_query = '''INSERT INTO friends 
#                     VALUES ('Merriwether', 'Lewis', 7)'''

# # if you have a bunch of variables to add in this is one way of doing it, but not the best way
# form_first = "Dana" # BAD! DON'T DO THIS
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
# c.execute(query)

# # the BETTER WAY if you have a bunch of variables to add in: 
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# # pass in a tuple containing the values that we want to be added in
# c.execute(query, (form_first,)) #if we didn't do it as a tuple it'd iterate over each char in string
# # *note that above form_first is a 1-item tuple, so we need the comma in the parameter "form_first,"

#HOWEVER, we would most often see a form like this:
data = ("Steve", "Irwin", 9) # *ALREADY in tuple form and grouped
query = "INSERT INTO friends VALUES (?,?,?)" # ?'s match columns match data

c.execute(query, data)
#commit changes
connection.commit()
connection.close() #close the connection at the end of script