# Requirements
# Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com

# You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, 
# the name of the person who said the quote, and the href of the link to the person's bio. 
# Store all of this information in a list.

# Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
# After each incorrect guess, the number of guesses remaining will decrement. 
# If the player gets to zero guesses without identifying the author, the player loses and the game ends. 
# If the player correctly identifies the author, the player wins!
# After every incorrect guess, the player receives a hint about the author. 
# For the first hint, make another request to the author's bio page (this is why we originally scrape this data),
# and tell the player the author's birth date and location.
# The next two hints are up to you! Some ideas: the first letter of the author's first name, 
# the first letter of the author's last name, the number of letters in one of the names, etc.
# When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. 
# If no, the program is complete.

currentQuoteNum=0
guesses = 5	

while True:

	# if entire page has been scraped, change currentURL (only after first page has been scraped) & scrapeThisPage() 
	# turn this into a function called "checkRescrape()"
	if currentQuoteNum == 10:
		print("Scrape quotes from next page.")

		# if isNext(soup):
		# 	currentURL = currentURL+get_next_link_end(soup)
		# else: currentURL = "https://quotes.toscrape.com/"
		# scrapeThisPage()

		#if THERE IS A NEXT PAGE
		#REFRESH ALL VARIABLES NEXT PAGES' URL
		#else REFRESH TO FIRST PAGE URL

	if guesses == 5: # if this is the first guess, then print quote
		print(f"Here’s a quote: quoteNum = {currentQuoteNum}")#+quotesList[currentQuoteNum])
		guesses-=1
	
	userGuess = input(f"Who said this? Guesses remaining: {guesses} \n").lower().strip()
	#case of user guessing correctly
	if userGuess == "Albert Einstein".lower():   #(they guess correctly)
		print("You guessed correctly! Congratulations!")
		while True:
			userChoice = input("Would you like to play again (y/n)? ").lower().strip()
			if userChoice == 'y': 
				guesses = 5
				currentQuoteNum+=1
				print("Great! Here we go again!")
				break		
			# GO BACK TO THE TOP OF THIS WHILE LOOP
			elif userChoice == 'n': 
				print("Ok! See you next time!")
				quit() 
			else: print("That was not a valid response!")
	# checkout Q5 here: https://pythongeeks.org/switch-in-python/ 
	elif guesses == 4: 
		print(f"Here’s a hint: getBio()")
		guesses-=1 #* getBio() requires quoteNum/soup object & returns String hint. 
		continue #at this point it needs to repose the question on line 44 above
	elif guesses == 3: 
		print(f"Here’s another hint: get2NDSTEPBio()")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		continue #at this point it needs to repose the question on line 44 above
	elif guesses == 2:
		print(f"Here’s another hint: get3rdSTEPBio()")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		continue #at this point it needs to repose the question on line 44 above
	elif guesses == 1:
		print(f"Here’s a final hint: FINAL HINT")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		continue #at this point it needs to repose the question on line 44 above	
	else: 
		print("You lose. Game over.")
		break
		
