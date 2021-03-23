import re


str='''
apple
banana
orange
peach
avocado
cherries
'''

pattern = r'.*s'    # Looking for something that ends in S
pattern_2 = r'\b[aeiou].+\b'    # Looking for a pattern that has aeiou
match = re.findall(pattern_2,str)

for m in match:
    print(m)