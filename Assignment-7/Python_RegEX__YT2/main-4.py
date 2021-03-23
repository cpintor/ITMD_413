import re

str = '''
Sam
car
2453
Alexa
John
90
'''

pattern = r'\b[A-Z][a-z]+\b'    # Getting rid of names
nstr = re.sub(pattern, "", str)    # Substituting words with null value

print(nstr)
