"""OK, now that we have Beautiful Soup installed, let's talk about what it is and what it isn't.
It allows us to navigate through and extract data from HTML using Python. But, and this is a big, big BUT, it does not download HTML for us.
#1 We have to manually make the request to get the data.
Let's say we're scraping IMDB, not saying it's a good idea to do that, but if we were and I was ... I don't know, scraping every single Web page I could find, spacing out the request by three seconds ... 
-I would use the *request module* to send a get request to one page, get the data back, and then I take that HTML that comes back.
I send it over to beautiful soup and I extract whatever information I want.
Maybe I'm trying to find links that I can crawl across and then send a further request to every link we get back from whoever Danny DeVito is Web page.
And then every link we get back from Danny DeVito page, we're then going to further scrape and keep going.
Anyway, my point is that beautiful soup does not download the HTML.
"""

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.body.div)
# d = soup.find("div")
# print(type(d)) # it's a bs4.element.Tag instance - it's own instance
#so when we parse HTML, beautiful soup takes that giant string 
#and turns each individual tag into it's own object
# d = soup.find_all(class_="special")
# d = soup.find_all(attrs={"data-example": "yes"})
# print(d)

#this part is for CSS
#d = soup.select("#first")[0]#gives first div & adding zero takes it out of list format
# d = soup.select(".special")
# d = soup.select("div")#select based off of a tag name
d = soup.select("[data-example]")#select based off of an attribute
print(d)
