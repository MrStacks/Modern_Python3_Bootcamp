#From video 365
import sqlite3

connection = sqlite3.connect("my_friends.db")

c = connection.cursor()

people = [
    ("Roald","Amundsen", 5), 
    ("Rosa","Parks", 8), 
    ("Henry","Hudson", 7),
    ("Neil","Armstrong", 7),
    ("Daniel","Boone", 3)]

'''2 ways to insert all of them as individual rows:
# 1: for person in people: 
#       insert that person
# 
# #2. c.executemany()'''

# this works (note that we had previously used "c.execute()")
# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# but if you want to do something else along with each call to execute()
# e.g., maybe you want to insert them into one table and then insert into another table
# e.g., or insert into one table and print it out
# e.g., you want to do math with part of your data as you are inserting
# e.g., you want to somehow collect pieces of data... e.g., take average of these
# .. especially if you have a ton of data, we do this: 
average = 0
for person in people: # will loop through 5x and do 5 separate inserts
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]
print(average/len(people))

# commit changes
connection.commit()
connection.close()