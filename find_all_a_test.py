import requests
from bs4 import BeautifulSoup

def get_b_days_places(urlLink):
	response = requests.get(urlLink)#request url & get html back

	soup = BeautifulSoup(response.text, "html.parser")

	bioLinksList = [] #List to hold links of each bio on page
	for link in soup.find_all('a'): #find all 'a' anchor tag
	    if '/author/' in link.get('href'): #if href (link) has '/author/' save link to biosList
	    	bioLinksList += [urlLink+link.get('href')] #was a list of chars, so I added []
	#save all birthdate/place as strings in a list
	bDatePlaceList = []
	for bioLink in bioLinksList:
		currentBio = requests.get(bioLink)
		bioSoup = BeautifulSoup(currentBio.text, "html.parser") #parse to soup object
		birthDate = bioSoup.find(class_="author-born-date").get_text() #get text of birthday
		birthPlace = bioSoup.find(class_="author-born-location").get_text() #get text of birthplace
		bDatePlaceList += [birthPlace +' '+ birthDate] #save birthplace/birthdate to one big string

	# return birthdates/birthplaces as List of birthdate+' '+birthplace strings	
	return bDatePlaceList

for datePlace in get_b_days_places("https://quotes.toscrape.com/"):
	print(datePlace)


############

# old version

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://quotes.toscrape.com/")#request url & get html back

# soup = BeautifulSoup(response.text, "html.parser")

# bioLinksList = [] #list to hold biosList
# for link in soup.find_all('a'): #find all 'a' anchor tag
#     if '/author/' in link.get('href'): #if href (link) has '/author/' save link to biosList
#     	bioLinksList += ['https://quotes.toscrape.com'+link.get('href')] #was a list of chars, so I added []
# #save all birthdate/place as strings in a list
# bDatePlaceList = []
# for bioLink in bioLinksList:
# 	currentBio = requests.get(bioLink)
# 	bioSoup = BeautifulSoup(currentBio.text, "html.parser") #parse to soup object
# 	birthDate = bioSoup.find(class_="author-born-date").get_text() #get text of birthday
# 	birthPlace = bioSoup.find(class_="author-born-location").get_text() #get text of birthplace
# 	bDatePlaceList += [birthPlace +' '+ birthDate] #save birthplace/birthdate to one big string

# for datePlace in bDatePlaceList:
# 	print(datePlace)

############ crap below	

# for element in biosList:
# 	print(element)  	

# bio1 = requests.get(biosList[0]) #get html of the first bio	

# bioSoup = BeautifulSoup(bio1.text, "html.parser") #parse to soup object

# birthDate = bioSoup.find(class_="author-born-date").get_text()
# birthPlace = bioSoup.find(class_="author-born-location").get_text()

# print('Hint: The author was born ' + birthDate, birthPlace + '.')


# for bio in bios:
# 	print("https://quotes.toscrape.com"+bio)


    # print(link.get('href'))	

# for each link in this list, save all of them that start with /author/    