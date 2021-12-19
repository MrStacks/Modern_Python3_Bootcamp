currentQuoteNum=0

while True:

	# if entire page has been scraped, change currentURL (only after first page has been scraped) & scrapeThisPage() 
	# turn this into a function called "checkRescrape()"
	if currentQuoteNum == 10:
		print("scrape quotes from next page")

		# if isNext(soup):
		# 	currentURL = currentURL+get_next_link_end(soup)
		# else: currentURL = "https://quotes.toscrape.com/"
		# scrapeThisPage()

		#if THERE IS A NEXT PAGE
		#REFRESH ALL VARIABLES NEXT PAGES' URL
		#else REFRESH TO FIRST PAGE URL

	guesses = 5	
	if guesses == 5: # if this is the first guess, then print quote
		print("Here’s a quote: bla bla bla")#+quotesList[currentQuoteNum])
	guesses-=1
	userGuess = input(f"Who said this? Guesses remaining: {guesses}").lower()
	#case of user guessing correctly
	if userInput == "Albert Einstein".lower():   #(they guess correctly)
		print("You guessed correctly! Congratulations!")
		userChoice = input("Would you like to play again (y/n)?").lower().strip()
		if userChoice == y: 
			print("Great! Here we go again!")
			continue		
		# GO BACK TO THE TOP OF THIS WHILE LOOP
		elif userChoice == n: 
			print("Ok! See you next time!")
			quit() 
		else: print("That was not a valid response!")
			# continue
			# GO BACK TO ASKING “Would you like to play again (y/n)?”
	elif guesses == 0: 
		print("You lose. Game over.")
		break
	elif guesses <= 4: 
		print(f"Here’s another hint: get2NDSTEPBio()")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		continue
	else: print(f"Here’s a hint: getBio()") #*Call getBio(), which requires quoteNum/soup object & returns String with hint. 
		guesses -=1
		continue 
	#GO BACK TO userGuess AT THIS POINT, BUT DO NOT PRINT A NEW QUOTE!!!!

# Great! Here we go again! 

# 	GO BACK TO THE TOP OF THIS WHILE LOOP
# 	(Call the “Here’s a quote: ” function again, but with a new quote number)


	currentQuoteNum+=1#do this at the end of the loop