class User:
    pass


# Creating objects
user1 = User()
user1.first_name = 'Dave'
user1.last_name = 'Jones'

# Accessing data same way it was assigned
print(user1.first_name)
print(user1.last_name)

# Creating a different user
user2 = User()
user2.first_name = 'Joe'
user2.last_name = 'Ken'

print(user2.first_name, user2.last_name)

# Attaching other fields to objects
user1.age = '34'
user2.favorite_book = 'Mobidick'




