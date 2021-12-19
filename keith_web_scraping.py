import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://quotes.toscrape.com/")#request url & get html back

soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 
# & tell it to parse and turn it into objects in Python
quotes = soup.find_all(class_="text")
authors = soup.find_all(class_="author") 

# get the rest of the 
URL = "https://quotes.toscrape.com/"
for page in range(2,11):
	req = requests.get(URL + "/page/" + str(page) + '/')
	soup2 = BeautifulSoup(req.text, 'html.parser')
	quotes += soup2.find_all(class_="text")
	authors += soup2.find_all(class_="author")

# change the bs4.element objects into Lists
quotesList = []
for quote in quotes:
	quotesList += quote.contents

authorsList = []
for author in authors:
	authorsList += author.contents

# print(quotesList[4])
# print(authorsList[4])

# dictionary = dict(zip(quotesList, authorsList))
# print(dictionary)

# MAKE THIS FOR 5 GUESSES TOTAL
# for q_num in range(0, len(quotesList)+1):
# 	print("Here's a quote:\n")
# 	print(quotesList[q_num])
# 	guess = str(input(f"\nWho said this? Guesses remaining: "))


while True:
  try:
    for q_num in range(0, len(quotesList)+1):
		print("Here's a quote:\n")
		print(quotesList[q_num])
		guesses = 5
		q_continue = "y"
		while q_continue != "n":
			guess = str(input(f"\nWho said this? Guesses remaining: {q_num}."))
			if guess == authorsList[q_num]:
				print("You guessed correctly! Congratulations!")
	      		q_continue = input("Would you like to play again (y/n)?").lower().strip()
		      	if q_continue == "y":
		      		print("Great! Here we go again...")
		      		continue
		      	elif q_continue == "n":
		      		print("Ok! See you next time!")
		      		quit()
		      	else: print("That wasn't a valid response.")		
    else: #TODO: This else must go - it has no if statement
    	guesses -= 1
      print(f"Here's a hint: {q_num}") #TODO: change to a hint scraped from the site 
      print(f"Guesses remaining: {guesses}")    
  except ValueError:
    print("Invalid")
    continue	


# After every incorrect guess, the player receives a hint about the author. 
# For the first hint, make another request to the author's bio page 
# (this is why we originally scrape this data), and tell the player 
# the author's birth date and location.
# The next two hints are up to you! Some ideas: the first letter of the 
# author's first name, the first letter of the author's last name, the 
# number of letters in one of the names, etc.	

# When the game is over, ask the player if they want to play again. 
# If yes, restart the game with a new quote. If no, the program is complete.
