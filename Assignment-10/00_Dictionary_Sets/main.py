"""
This program uses the Dictionary library
"""

Dict = {1:'Apple',2:'Strawberry',3:'Orange'}
print(Dict)
print(Dict[1])

Dict = {'Name':'Bob',1:[1,2,3,4]}
print(Dict)
print(Dict['Name'])

# Creating a new dictionary
Dict = {5:'Welcome',6:'To',7:'Geeks','A':{1:'Geeks',2:'For',3:'Geeks'},'B':{1:'Geeks',2:'Life'}}
print(Dict)

# Delete an item
del Dict[6]
print(Dict)

# Deleting subitem of A
del Dict['A'][2]
print(Dict)

# Popping
print(Dict.pop(5))

# Using pop item
print(Dict.popitem())

# Clear entire dictionary
Dict.clear()
print(Dict)

# Creating a new dictionary
Dict = {'key1':'Geeks','key2':'for'}
# Adding a new item to dict
Dict['key3'] = 'geeks'
print(Dict)

# Use update key
Dict.update(newkey1='is')
print(Dict)

# creating a new dictionary
stocks = {'IBM':234,'MSFT':44.56,'CSCO':'22.34'}
print(stocks)

for i in stocks:
    print(i)

for k,v in stocks.items():
    print('Code:{0}, Value:{1}' .format(k,v))