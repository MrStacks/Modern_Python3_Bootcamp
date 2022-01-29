'''Video 377 - SQL Injection!
'''
import sqlite3
connection = sqlite3.connect("users.db")
u = input("Please enter your username... ")
p = input("Please enter your password... ")

c = connection.cursor()

# # The WRONG way: 
# query = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'" 
# '''The [problem] is, because we're not parameterizing our inputs, we're 
# just sticking them directly into the SQL query, a user could actually 
# write SQL as part of their password.'''

 # Therefore, the RIGHT way (SQL library prevents malicious injections): 
query = f"SELECT * FROM users WHERE username=? AND password=?"
c.execute(query, (u,p))

result = c.fetchone()
if (result):
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")    

connection.commit()
connection.close()