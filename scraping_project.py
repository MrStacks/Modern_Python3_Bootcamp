# *there are multiple pages... and my hint to you is that you'll need to use a loop. 
# My strategy is to look at the "next" button.. you you want to 
# dynamnically look for that "next" button and if there is a next button, keep looping. 
# Otherwise, break out of the loop. 

# You're going to scrape all of the quotes, and for each one you should grab the text
# of the quote, the name of the person who said the quote, and the href of the link to 
# the person's bio

import requests
from bs4 import BeautifulSoup

originalURL = "https://quotes.toscrape.com/" #does not change
currentURL = "https://quotes.toscrape.com/" #will change as program runs
nextLinkEnd = "" # url end to the link for the next page
currentQuoteNum=0#holds List place of current quote/author/bioLink to iterate through all 3 Lists
guesses = 5
currentQuoteNum=0

#refreshes soup object, quotesList, authorsList, bioLinksList, & nextLinkEnd (if there is one)
def scrapeThisPage():
	#referesh all of the variables to everything scraped from current page
	soup = getSoup(currentURL)
	quotesList = quotesAuthors2List("text", soup)
	authorsList = quotesAuthors2List("author", soup)
	bioLinksList = getPageBiosURLs(soup, currentURL)
	nextLinkEnd = get_next_link_end(soup)
	currentQuoteNum=0 #refresh so that we can start iterating through the Lists again
return

while True:
	# if entire page has been scraped, change currentURL (only after first page has been scraped) & scrapeThisPage() 
	# turn this into a function called "checkRescrape()"
	if currentQuoteNum == 10:
		#GO TO NEXT PAGE
		scrapeThisPage()
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
		print(f"Here’s a hint: {getBio()}")
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
		

#scrapes current page (soup object) html for all quotes/authors
#TODO: add this hints links?????
# 1st arg is name of the class that holds thing we want ()
def quotesAuthors2List(className, soupObject):
	found = soupObject.find_all(class_=className)
	thingList = []
	for thing in found:
		thingList += thing.contents
	return thingList

#TODO get the CURRENT URL
def getPageBiosURLs(soupObject, currentURL):
	bioLinksList = [] #List to hold links of each bio on page
	for link in soup.find_all('a'): #find all 'a' anchor tag
	    if '/author/' in link.get('href'): #if href (link) has '/author/' save link to biosList
	    	bioLinksList += [currentURL+link.get('href')] #was a list of chars, so I added []
	 return bioLinksList   		

# returns birthdate/birthplace as a single String
def getBio(currentQuoteNum, bioLinksList, currentURL):
	bioLink = currentURL[1:]+bioLinksList[currentQuoteNum] #save link to bio
	currentBio = requests.get(bioLink) #get bioLink HTML
	bioSoup = BeautifulSoup(currentBio.text, "html.parser") #parse to soup object
	birthDate = bioSoup.find(class_="author-born-date").get_text() #get text of birthday
	birthPlace = bioSoup.find(class_="author-born-location").get_text() #get text of birthplace
	bDatePlace = birthPlace +' '+ birthDate #save birthplace/birthdate to one string
	return bDatePlace # return birthdate/birthplace as a single String

# returns html soup object from URL specified in domain name
# 2nd (optional) arg used whenever we want a site with a path beyond original domain
def getSoup(originalURL, nextLinkEnd=None):
	if isNext:# note that I removed "/" on end of the URL on next line
		response = requests.get(originalURL[1:]+nextLinkEnd)#get html for next link
	else: response = requests.get(originalURL)# get html for first link
	soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 
	return soup

def get_next_link_end(soupObject):
	if soupObject.find(class_="next"): #if there is a "next" button on this page
		linkEnd = soupObject.find(class_="next").find('a').get('href') #save the link extension for it
	return linkEnd #return the link extension	

# This is probably redundant
def isNext(soupObject):
	nextTrial = get_next_link_end(soupObject)
	if nextTrial != None:
		return True
	return False
		

