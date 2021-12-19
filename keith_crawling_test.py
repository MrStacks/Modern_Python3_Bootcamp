import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")#request url & get html back

soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 
# & tell it to parse and turn it into objects in Python
links = soup.find(class_="author").find_next_sibling()

# change it to a List ????
linksList = []
for link in links:
	linksList += link

print(links)	

# print(str(linksList[0]).split('"')[1::2])

# <a href="/author/Albert-Einstein">(about)</a>
# *Then somehow cut everything out of the quotations

# for link in links:
# 		print(link)