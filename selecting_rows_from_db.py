# Video 366: Selecting with Python

import sqlite3

connection = sqlite3.connect("my_friends.db")
# create cursor object
c = connection.cursor()
# let's say I want to SELECT * every friend in the db
# c.execute("SELECT * FROM friends")

'''To print this, we can't do "print(c)" b/c it returns a cursor object, 
unless we do a for-loop '''
# for result in c:
#     print(result) # returns rows of 1 tuple/row per friend/name
'''But if we want it all in the form of a list.. & if we were trying to do 
something else with them, e.g., batch insert into another table where you
wanted them in a list for some reason, this is how you'd do that:'''
# print(c.fetchall()) # gives us a list that contains all of the results 

'''Alternatively, if you just want one of the results:'''
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
# print(c.fetchone()) # assuming I just want the 1st Rosa 

'''close greater than 5, order by how close, and fetchall'''
c.execute("SELECT * FROM friends WHERE close > 5 ORDER BY close")
print(c.fetchall())


# commit changes
connection.commit()

# the above commands look the same as what we have seen
# in this case we'll get something back, however
connection.close()

'''Next video: dynamic queries'''