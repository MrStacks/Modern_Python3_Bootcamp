# *there are multiple pages... and my hint to you is that you'll need to use a loop. 
# My strategy is to look at the "next" button.. you you want to 
# dynamnically look for that "next" button and if there is a next button, keep looping. 
# Otherwise, break out of the loop. 

# You're going to scrape all of the quotes, and for each one you should grab the text
# of the quote, the name of the person who said the quote, and the href of the link to 
# the person's bio

import requests
from bs4 import BeautifulSoup

originalURL = "https://quotes.toscrape.com/"
currentURL = "https://quotes.toscrape.com/" #will change as program runs
nextLinkEnd = "" # url end to the link for the next page
currentQuoteNum=0#holds List place of current quote/author/bioLink to iterate through all 3 Lists

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

#call at beginning of program, & again when currentQuoteNum=10 (inside while loop)
scrapeThisPage()

while True:

	# if entire page has been scraped, change currentURL (only after first page has been scraped) & scrapeThisPage() 
	# turn this into a function called "checkRescrape()"
	if currentQuoteNum == 10:
		if isNext(soup):
			currentURL = currentURL+get_next_link_end(soup)
		else: currentURL = "https://quotes.toscrape.com/"
		scrapeThisPage()

		#if THERE IS A NEXT PAGE
		#REFRESH ALL VARIABLES NEXT PAGES' URL
		#else REFRESH TO FIRST PAGE URL

	guesses = 5	
	print("Here’s a quote: "+quotesList[currentQuoteNum])
	guesses-=1
	userGuess = input(f"Who said this? Guesses remaining: {guesses}").lower()



	if userInput == authorsList[currentQuoteNum].lower():   #(they guess correctly)
		print("You guessed correctly! Congratulations!")
		userChoice = input("Would you like to play again (y/n)?").lower().strip()
		if userChoice == y: print("Great! Here we go again!")
		break
		# GO BACK TO THE TOP OF THIS WHILE LOOP
	elif userChoice == n: 
		print("Ok! See you next time!")
		quit() 
	else: print("That was not a valid response!")
		# GO BACK TO ASKING “Would you like to play again (y/n)?”
else:    #(they guess incorrectly)
	if guesses == 0: 
		print("You lose. Game over.")
		quit()
	guesses -=1
	print(f"Here’s a hint: {getBio()}") #*Call getBio(), which requires quoteNum/soup object & returns String with hint. 
	#TAKE INPUT AGAIN AND, ONCE SUBMITTED, TEST IT AGAIN

# Great! Here we go again! 

# 	GO BACK TO THE TOP OF THIS WHILE LOOP
# 	(Call the “Here’s a quote: ” function again, but with a new quote number)


	currentQuoteNum+=1#do this at the end of the loop
	

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
		

