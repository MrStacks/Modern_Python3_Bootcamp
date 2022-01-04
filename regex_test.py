import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match: 
        return match.group()
    else: 
        return None
    
print(extract_phone("my number is 432 567-8976"))
print(extract_phone("my number is 432 567-897622"))