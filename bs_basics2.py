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
# el = soup.select(".special")[0]#select all items that have class "special", & narrow to first one [0]
# print(el.get_text())#extracts text only ~ useful 4 extracting specific data
# for el in soup.select(".special"):#everything that has the class "special"
#   print(el.get_text()) #should give us inner text for all items

# for el in soup.select(".special"):
#   print(el.name)#should refer to the name of tag (like li)
  #so 4 everything that has class name "special" we're going to print the name

#Hopefully by now you can start to see how these things work together
#we iterate over them and extract something for each one.. 
#get_text() is really commonly used

# for el in soup.select(".special"):
#   print(el.name)
#   print(el.attrs)#a dictionary containing key value pairs for attributes on each item
#   #but the above is probably redundant 
#let's say I want to select the h3 above
# attr = soup.find("h3")["data-example"]
# print(attr)
#we could do the same thing with div:
attr = soup.find("div")["id"]#this syntactical shortcut 
#can be used to directly access attributes to get their values 
#if we have the key, but you can also call .attrs to get a 
#dictionary containing all key-value attributes
print(attr)
# print(el)