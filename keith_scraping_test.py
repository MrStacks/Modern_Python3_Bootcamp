import requests
from bs4 import BeautifulSoup

biosList = []
quotesList = []
authorsList = []

response = requests.get("https://quotes.toscrape.com/")#request url & get html back

soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 

# & tell it to parse and turn it into objects in Python
quotes = soup.find_all(class_="text")
authors = soup.find_all(class_="author")
for link in soup.find_all('a'):
    if "/author/" in link.get('href'):
    	biosList += ["https://quotes.toscrape.com"+link.get('href')]

# for link in soup.find_all('a'):
#     if "/author/" in link.get('href'):
#     	bios += link.get('href') 

# get the rest of the 
URL = "https://quotes.toscrape.com/"
for page in range(2,11):
	req = requests.get(URL + "/page/" + str(page) + '/')
	soup2 = BeautifulSoup(req.text, 'html.parser')
	quotes += soup2.find_all(class_="text")
	authors += soup2.find_all(class_="author")
	for link in soup2.find_all('a'):
		if "/author/" in link.get('href'):
			biosList += ["https://quotes.toscrape.com"+link.get('href')]

# change the bs4.element objects into Lists
for quote in quotes:
	quotesList += quote.contents
for author in authors:
	authorsList += author.contents

# print(quotesList[4])
print(quotesList[0], authorsList[0], biosList[0])

# dictionary = dict(zip(quotesList, authorsList))
# print(dictionary)

