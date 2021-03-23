import re

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') # same pattern as above but number specifies the no. of /d

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)

with open('data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match)


