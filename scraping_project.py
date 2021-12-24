# *there are multiple pages... and my hint to you is that you'll need to use a loop. 
# My strategy is to look at the "next" button.. you you want to 
# dynamnically look for that "next" button and if there is a next button, keep looping. 
# Otherwise, break out of the loop. 

# You're going to scrape all of the quotes, and for each one you should grab the text
# of the quote, the name of the person who said the quote, and the href of the link to 
# the person's bio

import requests
from bs4 import BeautifulSoup

original_URL = "https://quotes.toscrape.com/" #does not change
current_URL = "https://quotes.toscrape.com/" #will change as program runs
next_link_end = "" # url end to the link for the next page
current_quote_num=0#holds List place of current quote/author/bio_link to iterate through all 3 Lists
guesses = 5
current_quote_num=0


#scrapes current page (soup object) html for all quotes/authors
#TODO: add this hints links?????
# 1st arg is name of the class that holds thing we want ()
def quotesAuthors2List(class_name, soup_object):
	found = soup_object.find_all(class_=class_name)
	thing_list = []
	for thing in found:
		thing_list += thing.contents
	return thing_list

#TODO get the CURRENT URL
def getPageBiosURLs(soup_object, current_URL):
	bio_links_list = [] #List to hold links of each bio on page
	for link in soup.find_all('a'): #find all 'a' anchor tag
	    if '/author/' in link.get('href'): #if href (link) has '/author/' save link to biosList
	    	bio_links_list += [current_URL+link.get('href')] #was a list of chars, so I added []
	return bio_links_list   		

# returns birthdate/birthplace as a single String
def get_bio(current_quote_num, bio_links_list, current_URL):
	bio_link = current_URL[1:]+bio_links_list[current_quote_num] #save link to bio
	current_bio = requests.get(bio_link) #get bio_link HTML
	bio_soup = BeautifulSoup(current_bio.text, "html.parser") #parse to soup object
	birth_date = bio_soup.find(class_="author-born-date").get_text() #get text of birthday
	birth_place = bio_soup.find(class_="author-born-location").get_text() #get text of birthplace
	b_date_place = birth_place +' '+ birth_date #save birthplace/birthdate to one string
	return b_date_place # return birthdate/birthplace as a single String

# returns html soup object from URL specified in domain name
# 2nd (optional) arg used whenever we want a site with a path beyond original domain
def get_soup(original_URL, next_link_end=None):
	if is_next:# note that I removed "/" on end of the URL on next line
		response = requests.get(original_URL[1:]+next_link_end)#get html for next link
	else: response = requests.get(original_URL)# get html for first link
	soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 
	return soup

def get_next_link_end(soup_object):
	if soup_object.find(class_="next"): #if there is a "next" button on this page
		link_end = soup_object.find(class_="next").find('a').get('href') #save the link extension for it
	return link_end #return the link extension	

# This is probably redundant
def is_next(soup_object):
	next_trial = get_next_link_end(soup_object)
	if next_trial != None:
		return True
	return False
		

#refreshes soup object, quotes_list, authors_list, bio_links_list, & next_link_end (if there is one)
def scrape_this_page():
	#referesh all of the variables to everything scraped from current page
	soup = get_soup(current_URL)
	quotes_list = quotesAuthors2List("text", soup)
	authors_list = quotesAuthors2List("author", soup)
	bio_links_list = getPageBiosURLs(soup, current_URL)
	next_link_end = get_next_link_end(soup)
	current_quote_num=0 #refresh so that we can start iterating through the Lists again
	return True

scrape_this_page()	

while True:
	# if entire page has been scraped, change current_URL (only after first page has been scraped) & scrape_this_page() 
	# turn this into a function called "checkRescrape()"
	if current_quote_num == 10:
		#GO TO NEXT PAGE
		scrape_this_page()
		# if is_next(soup):
		# 	current_URL = current_URL+get_next_link_end(soup)
		# else: current_URL = "https://quotes.toscrape.com/"
		# scrape_this_page()

		#if THERE IS A NEXT PAGE
		#REFRESH ALL VARIABLES NEXT PAGES' URL
		#else REFRESH TO FIRST PAGE URL

	if guesses == 5: # if this is the first guess, then print quote
		print(f"Here’s a quote: quoteNum = {quotes_list[current_quote_num]}")#+quotes_list[current_quote_num])
		guesses-=1
	
	userGuess = input(f"Who said this? Guesses remaining: {guesses} \n").lower().strip()
	#case of user guessing correctly
	if userGuess == "Albert Einstein".lower():   #(they guess correctly)
		print("You guessed correctly! Congratulations!")
		while True:
			userChoice = input("Would you like to play again (y/n)? ").lower().strip()
			if userChoice == 'y': 
				guesses = 5
				current_quote_num+=1
				print("Great! Here we go again!")
				break		
			# GO BACK TO THE TOP OF THIS WHILE LOOP
			elif userChoice == 'n': 
				print("Ok! See you next time!")
				quit() 
			else: print("That was not a valid response!")
	# checkout Q5 here: https://pythongeeks.org/switch-in-python/ 
	elif guesses == 4: 
		print(f"Here’s a hint: {get_bio()}")
		guesses-=1 #* get_bio() requires quoteNum/soup object & returns String hint. 
		#at this point it needs to repose the question on line 44 above
	elif guesses == 3: 
		print(f"Here’s another hint: get2NDSTEPBio()")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		#at this point it needs to repose the question on line 44 above
	elif guesses == 2:
		print(f"Here’s another hint: get3rdSTEPBio()")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		#at this point it needs to repose the question on line 44 above
	elif guesses == 1:
		print(f"Here’s a final hint: FINAL HINT")#TODO SECOND STAGE HINTING HERE
		guesses -=1	
		#at this point it needs to repose the question on line 44 above	
	else: 
		print("You lose. Game over.")
		break
		
  