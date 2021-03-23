# Printing out dictionary values using F-string

person = {'name': 'Jenn', 'age': 23} # Dictionary

# # Using format()
# sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
# print(sentence)

# Using F-String
sentence = f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence)