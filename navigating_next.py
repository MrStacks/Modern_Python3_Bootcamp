import requests
from bs4 import BeautifulSoup

def get_next_link_end(hostURL):
	
	response = requests.get(hostURL)#request url & get html back
	soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 

	if soup.find(class_="next"): #if there is a "next" button on this page
		linkEnd = soup.find(class_="next").find('a').get('href') #save the link extension for it
	return linkEnd #return the link extension

def get_all_page_links(hostURL):
	response = requests.get(hostURL)#request url & get html back
	soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 
	allLinks = [hostURL] #add the first url to the links list, but only do this once!
	
	if soup.find(class_="next"): # if there is a "next" link (prevents infinite loop)
		isNext = True
	nextLinkEnd = None 
	while isNext: #if there is a "next" button on this page
		if nextLinkEnd: #if we have a new link to a new page, use it
			nextLinkEnd = get_next_link_end(hostURL+nextLinkEnd)[1:] #get link end (for next link) at "next" button
		else: nextLinkEnd = get_next_link_end(hostURL)[1:]# use original URL (only happens on 1st iteration)
		allLinks += [hostURL+nextLinkEnd] #add link end + original link to list of all links
		nextResponse = requests.get(hostURL+nextLinkEnd)#request next link to go there
		# nextLinkEnd2 = nextLinkEnd
		soup2 = BeautifulSoup(nextResponse.text, "html.parser")#give it to BeautifulSoup
		if soup2.find(class_="next"):
			isNext = True
		else: isNext = False
	return allLinks	

print(get_all_page_links("https://quotes.toscrape.com/"))


# for link in soup.find_all('a'):
#     print(link.get('href'))
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie