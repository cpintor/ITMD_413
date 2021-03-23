"""
Write a program that will convert such lines to a Lightweight Directory Access Protocol (LDAP)
record format as shown below:
dn: uid=Username, dc=example, dc=com
cn: Firstname Lastname
sn: Lastname
telephoneNumber: Telephone number

Name: Cristian Pintor
"""
import re

email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
fname_pattern = re.compile(r':(.*)')
phone_pattern = re.compile(r'\d{10}')



with open('data.txt', 'r') as file:
    contents = file.read()

    matches_email = email_pattern.findall(contents)
    matches_fname = fname_pattern.findall(contents)
    matches_phone = phone_pattern.findall(contents)

    for match in matches_email:
        print(match)

    for match in matches_fname:
        print(match)

    for match in matches_phone:
        print(match)


