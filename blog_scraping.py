# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer
# We're going to make a request, get the response back, 
# take the html we get back, send it to BeautifulSoup, then navigate
# through that, extract info we want, & write it to a file using csv

response = requests.get("https://www.rithmschool.com/blog")#request url & get html back

# print(response.text) #this was first thing we did to see the html

soup = BeautifulSoup(response.text, "html.parser")#give it to BeautifulSoup 
# & tell it to parse and turn it into objects in Python
articles = soup.find_all("article")#call find_all on result (soup) to find all articles
# ideally we'll have them all in a collection - &, yes, comes as one giant List w every "article"

# now we want the title of each article, which is text inside of the anchor tag
# *because it's the first anchor tag, we can just call .find() rather than .find_all() (VERY INTERESTING)
# THUS: 
# for article in articles:
# 	print(article.find("a"))#gives us all the anchor tags
# but what we want is the text inside the anchor tags:	

# for article in articles: # MOMENT OF TRUTH
# 	print(article.find("a").get_text()) # THIS WORKS & GIVES ALL TITLES
# next step on line 34

with open("blog_data.csv", "w") as csv_file:
	csv_writer = writer(csv_file) #gives us the CSV writer with that file blog data
	csv_writer.writerow(["title", "link", "date"])
	for article in articles: 
		a_tag = article.find("a") #save article.find("a") (anchor tag)
		title = a_tag.get_text() #save get_text() to variable
		url = a_tag['href'] #gives us URL
		date = article.find("time")["datetime"]
		csv_writer.writerow([title, url, date])

# scraping portion complete at this point. 
# now to write it to CSV (done on lines 30 & 31)




