import re

str = '''
dfshj@gmail.com
3ytgdg.56
tigacharm56h@hotmail.com
hfg123h@aol
'''

pattern = r'[a-z]+[0-9]*[a-z]*@[a-z]+\.com'  # pattern to look for valid email
match = re.findall(pattern, str)
match_2 = re.finditer(pattern,str)  # finds more information

for m in match_2:
    print(m)
    print(m.span()) # to view the span()
