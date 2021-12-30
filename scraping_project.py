# Assignment: "There are multiple pages... and my hint to you is that you'll need to use a loop. 
# My strategy is to look at the "next" button.. you you want to dynamnically look for that 
# "next" button and if there is a next button, keep looping. Otherwise, break out of the loop. 
# You're going to scrape all of the quotes, and for each one you should grab the text
# of the quote, the name of the person who said the quote, and the href of the link to 
# the person's bio

import requests
from bs4 import BeautifulSoup
from re import sub

original_URL = "https://quotes.toscrape.com/" #does not change
current_url = "https://quotes.toscrape.com/" #will change as program runs
next_link_end = "" # url end to the link for the next page
current_quote_num = 0#holds List place of current quote/author/bio_link to iterate through all 3 Lists
guesses = 5
global soup

#scrapes current page (soup object) html for all quotes/authors
#TODO: add this hints links?????
# 1st arg is name of the class that holds thing we want ()
def soup_object_to_list(class_name, soup_object):
	found = soup_object.find_all(class_=class_name)
	thing_list = []
	for thing in found:
		thing_list += thing.contents
	return thing_list

# TODO describe
def get_bios_urls(soup_object, current_url):
	bio_links_list = [] #List to hold links of each bio on page
	for link in soup_object.find_all('a'): #find all 'a' anchor tag
	    if '/author/' in link.get('href'): #if href (link) has '/author/' save link to biosList
	    	bio_links_list += [current_url[:-1]+link.get('href')] #was a list of chars, so I added []
	return bio_links_list   		

# returns birthdate/birthplace as a single String
def get_bio(current_quote_num, bio_links_list):
    bio_link = bio_links_list[current_quote_num] #save link to bio
    current_bio = requests.get(bio_link) #get bio_link HTML
    bio_soup = BeautifulSoup(current_bio.text, "html.parser") #parse to soup object
    birth_date = bio_soup.find(class_="author-born-date").get_text() #get text of birthday
    birth_place = bio_soup.find(class_="author-born-location").get_text() #get text of birthplace
    b_date_place = birth_place +' '+ birth_date #save birthplace/birthdate to one string
    author_description = bio_soup.find(class_="author-description")
    author_bio = [b_date_place, author_description]
    return author_bio # return birthdate/birthplace as a single String

# TODO describe
def get_soup(url):
	response = requests.get(url)# get html for first link
	return BeautifulSoup(response.text, "html.parser")# return soup object 

# TODO describe
def get_next_link_end(soup_object):
	if soup_object.find(class_="next"): #if there is a "next" button on this page
		link_end = soup_object.find(class_="next").find('a').get('href') #save the link extension for it
	return link_end #return the link extension	

# TODO describe
def is_next(soup_object):
	next_trial = get_next_link_end(soup_object)
	if next_trial != None:
		return True
	return False

#refreshes soup object, quotes_list, authors_list, bio_links_list, & next_link_end (if there is one)
def scrape_this_page():
    #referesh all of the variables to everything scraped from current page
    global quotes_list #NOTE in video 336, he uses a dictionary to hold these
    global authors_list #NOTE he says in real life it's better to save quotes to a file (JSON, CSV, or Pickle file)
    global bio_links_list
    global next_link_end
    global current_quote_num
    soup = get_soup(current_url)
    quotes_list = soup_object_to_list("text", soup)
    authors_list = soup_object_to_list("author", soup)
    bio_links_list = get_bios_urls(soup, current_url)
    next_link_end = get_next_link_end(soup)
    current_quote_num = 0 #refresh so that we can start iterating through the Lists again
    print(authors_list)
    return True
    # He does:
    # def scrape_quotes():
        # response = requests.get(current_url)# get html for first link
        # soup =  BeautifulSoup(response.text, "html.parser")
        # quotes = soup.find_all(class_="quote")
        # all_quotes = []
        # for quote in quotes:
        #     all_quotes.append({
        #         "text": quote.find(class_="text").get_text(),
        #         "author": quote.find(class_="author").get_text(),    
        #         "bio-link": quote.find(class_="a")["href"]
        #     })
        # next_button = soup.find(class_="next")
        # url = next_button.find("a")["href"] if next_button else None  
        # return all_quotes 

#scrape page/initialize all global variables so they can be used 
scrape_this_page()	

# TODO describe the game logic
while True:
    # if entire page has been scraped, check if there is a next page and, if so, scrape it 
	# else go back to original page (start scraping series of pages all over again)
    if current_quote_num == 10:
        # update current_url
        if is_next(soup): current_url = current_url+get_next_link_end(soup)
        else:
        	current_url = "https://quotes.toscrape.com/"
        scrape_this_page()
    # if this is the first guess, then print quote      
    if guesses == 5: 
        print(f"Here’s a quote: {quotes_list[current_quote_num]}")
        guesses -= 1
    # todo: deal with case of "André Gide" input
    userGuess = input(f"Who said this? Guesses remaining: {guesses} ").lower().strip()
    
    if userGuess == authors_list[current_quote_num].lower(): # user guesses correctly
        print("You guessed correctly! Congratulations!")
        # TODO I could make this into a function called "ask_replay()"
        while True:
            userChoice = input("Would you like to play again (y/n)? ").lower().strip()
            if userChoice == 'y': 
                guesses = 5
                current_quote_num += 1
                print("Great! Here we go again!")
                break
            elif userChoice == 'n':
                print("Ok! See you next time!")
                quit()
            else: print("That was not a valid response!")
    	# checkout Q5 here: https://pythongeeks.org/switch-in-python/         
    elif guesses == 4:
        global current_bio
        current_bio = get_bio(current_quote_num, bio_links_list)
        print(f"Here’s a hint: The author was born {current_bio[0]}")
        guesses -= 1 #* get_bio() requires quoteNum/soup object & returns String hint.
    elif guesses == 3:
        authors_name = authors_list[current_quote_num]
        initals = authors_name[0] +'. ' + authors_name.split(" ")[1][0] +'. ' # note 2nd initial [1] = last name & [0] = 1st initial
        print(f"Here’s another hint: The authors initials are: {initals}")
        guesses -=1
    elif guesses == 2: #TODO remove authors' name... or I could remove this altogether
        # long_bio_string = current_bio[1].replace(authors_list[current_quote_num], '[the author]')
        # long_bio_string = sub(authors_list[current_quote_num], '[the author]', current_bio[1])
        # print(f"Here’s another hint: {long_bio_string}") 
        print(f"Here’s another hint: {current_bio[1]}")     
        guesses -= 1
    elif guesses == 1:
        print(f"No more hints, but you have one last try! ")#TODO 
        guesses -= 1
    else:
        print(f"The answer was {authors_list[current_quote_num]}")
        # TODO I could make this into a function called "ask_replay()"
        userChoice = input("Would you like to play again (y/n)? ").lower().strip()
        while True:
            if userChoice == 'y': 
                guesses = 5
                current_quote_num+=1
                print("Great! Here we go again!")
                break
            elif userChoice == 'n':
                print("Ok! See you next time!")
                quit()
            else: print("That was not a valid response!")
        
		
  