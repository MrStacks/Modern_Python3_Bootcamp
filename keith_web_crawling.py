import requests
from bs4 import BeautifulSoup

# We're going to make a request, get the response back, 
# take the html we get back, send it to BeautifulSoup, then navigate
# through that, extract info we want, & write it to a file using csv

# result = requests.get("https://quotes.toscrape.com/")#request url & get html back

# # print(result.status_code)
# # print(result.headers)

# src = result.content
# soup = BeautifulSoup(src, 'lxml')
# links = soup.find_all("a")
# for link in links:
# 	print(link.attrs['href'])



URL = "https://quotes.toscrape.com/"

for page in range(2,5):
	req = requests.get(URL + "/page/" + str(page) + '/')
	soup = BeautifulSoup(req.text, 'html.parser')
	quotes = soup.find_all(class_="text")
	authors = soup.find_all(class_="author")
	for quote in quotes:
		print(quote.contents[0])
	for author in authors:
		print(author.contents[0])

