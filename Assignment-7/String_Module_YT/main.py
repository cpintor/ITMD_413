# F-Strings - How to Use Them and Advanced String Formatting

first_name = 'Corey'
last_name = 'John'

# Without using F-string (I think)
# sentence = 'My name is {} {}'.format(first_name, last_name)
# print(sentence)

# Using F-String
sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)