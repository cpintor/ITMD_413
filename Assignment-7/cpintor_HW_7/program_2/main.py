"""
This program takes phone number inputs from user and matches it with the correct pattern.

Name: Cristian Pintor
"""

import re


phone = input('Please enter phone number: ')

pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})') # Looking for this pattern
pattern2 = re.compile(r'[.\d{3}.\d{7}]')


matches = pattern.findall(phone) #


for match in matches:
    print('First',match)

if re.search(pattern, phone):
    print('Valid phone number')

    num = re.sub(r'\D', "", phone)
    print('Using num', num)

    new_pattern = re.compile(r'[0-9]+')

    new_format = re.findall(new_pattern, match)

    print(new_format)

    print('No hyphens',new_format)



    for format in new_format:
        print(format)

    # print('New phone format:',new_format[0],new_format[1],new_format[2])


else:
    print('Invalid email, try again')