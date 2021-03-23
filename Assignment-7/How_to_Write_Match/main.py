import re

text_to_search = '''
abcdefghijklmnopqrztvuwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentance and then bring it to an end'

pattern = re.compile(r'abc')    # pattern looking for abc
pattern_2 = re.compile(r'coreyms\.com')  # pattern escaping the .
pattern_3 = re.compile(r'\BHa') # \B matches Has that do not have a word boundary before it

pattern_4 = re.compile(r'^Start')   # Looking for literal text Start at beginning of sentence
pattern_5 = re.compile(r'end$')   # Looking for literal text end at end of sentence


matches = pattern_2.finditer(text_to_search)
# matches = pattern_5.finditer(sentence)

for match in matches:
    print(match)

