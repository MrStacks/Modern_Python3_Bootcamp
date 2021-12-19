
# requires pip install requests @ docs.python-requests.org

import requests
from random import choice


topic = input("Let me tell you a joke! Give me a topic: ")

results = requests.get(
	"https://icanhazdadjoke.com/search", 
	headers={"Accept": "application/json"},
	params={"term": topic}
).json() # obtain results in json

num_jokes = results["total_jokes"]

res_index = results["results"]

if num_jokes == 0:
	print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
elif num_jokes == 1:
	print(f"I've got one joke about {topic}. Here's one:")
	print(res_index[0]["joke"]) 
else:
	print(f"I've got {num_jokes} jokes about {topic}. Here's one:")
	print(choice(res_index)["joke"]) # randomly choose one joke





