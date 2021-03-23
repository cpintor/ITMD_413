import re

text_to_search = '''
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''


# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')    # matching Mr
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # matching and r, s, or rs

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)