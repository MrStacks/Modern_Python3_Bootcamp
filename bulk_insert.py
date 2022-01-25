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

# note that we had previously used "c.execute() for a single variable"
c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# commit changes
connection.commit()
connection.close()


#LOOK UP sqlite to dataframe in pandas so that I can see how ...