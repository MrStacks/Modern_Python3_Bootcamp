import re

url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")
# # gives the whole URL
# print(match.group())
# # returns tuple with protocol, base URL, and additional info all separate
# print(match.groups())

# # gives individual group
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))
# print(match.group(3))

print(f"Protocol: {match.group(1)}")
print(f"Domain: {match.group(2)}")
print(f"Everything else: {match.group(3)}")