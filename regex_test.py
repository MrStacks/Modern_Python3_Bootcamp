import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match: 
        return match.group()
    else: 
        return None
    
# print(extract_phone("my number is 432 567-8976"))
# print(extract_phone("my number is 432 567-897622"))
# print(extract_phone("432 567-8976 adsfadf"))
# print(extract_phone("432 567-8976"))    
    
def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)   
    
# print(extract_all_phones("my number is 432 567-8976 or call me at 347 666-7899"))
# print(extract_all_phones("my number is 432 56"))

# regex.search version 
# def is_valid_phone(input):
#     phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     match = phone_regex.search(input)
#     if match: 
#         return True 
#     return False

# regex.fullmatch version doesn't require ^ and $ on ends
def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match: 
        return True 
    return False

print(is_valid_phone("432 567-8976"))    
print(is_valid_phone("432 567-8976 ads"))    
print(is_valid_phone("asd 432 567-8976 d"))    

