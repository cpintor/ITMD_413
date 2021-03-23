import re

str = 'Abcd 4 computer 765 Python 687'

pattern = 'computer'    # word to be extracted from string
match = re.findall(pattern, str)
print(match)


pattern_2 = r'[a-zA-Z]+'    # raw string that get rids of anything with numbers
pattern_3 = r'[0-9]+'   # Only numbers
pattern_4 = r'[a-zA-Z0-9]'  # Letters and numbers
pattern_5 = r'[^ ]+'    # Looking for blank space
match_2 = re.findall(pattern_3, str)
print(match_2)