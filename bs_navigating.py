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
    <li class="special super_special">This list item is special.</li>
    <li>This list item is not special.</li>
    <li class="special">This list item is also special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# data = soup.body.contents #selects <body> above, 
# # & then the contents of <body> in List format 
# print(data)
# **BUT notice the /n whenever there is a break between elements
# (assuming they are on different lines)

# So "contents" gives us that List, and if I wanted to find the
# first child/descendent of the body, I would need to access [1]:
# data = soup.body.contents[1]#an example of "navigating to the thing we want"

#then we can focus on the contents of that:
# data = soup.body.contents[1].contents#essentially removes the <div> x2
# data = soup.body.contents[1].next_sibling#calls sibling of <div> (<ol>in this case)
# #but the problem is that it treats the '\n' as the next sibling... therefore:
# data = soup.body.contents[1].next_sibling.next_sibling #call it again
# &, as another approach, we could also do:
# data = soup.find(class_="super_special")# gives us the <li> (step 1)
# data = soup.find(class_="super_special").parent #gives us <ol> that encloses <li>
# data = soup.find(class_="super_special").parent.parent #move up another layer (entire body)
# So that was what we've already seen -> navigating via tags

# There's also a subset of methods we can use where we can search:
# find_parent / find_parents
# find_next_sibling / find_next_siblings
# find_previous_sibling / find_previous_siblings

# data = soup.find(id="first").find_next_sibling()#finds next object ..
# .. rather than next newline (as next_sibling would have done)

# data = soup.find(id="first").find_next_sibling().find_next_sibling()
# & (as shown above) we can chain them together to keep moving forward

# data = soup.select("[data-example]")[1].find_previous_sibling()

# Another thing to mention: when we use find_previous_sibling(), we can
# actually pass in a String. (He first switches up the <li> classes @9:45, video332)

# data = soup.find(class_="super_special").find_next_sibling()
# data = soup.find(class_="super_special").find_next_sibling(class_="special")

# data = soup.find("h3").find_parent()#starts at h3 & moves up to print entire parent


print(data)





















