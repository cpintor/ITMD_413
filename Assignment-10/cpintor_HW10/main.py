"""
This program keeps names and email addresses in a dictionary as key value pairs
Name: Cristian Pintor
"""

import pickle

entry = 'y'

while entry == 'y':

    pickle_in = open("dict.pickle", "rb")
    # data = pickle.load(pickle_in)
    # print(pickle_in)

    print('1. Add a new name and email address')
    print('2. Find an email address')
    print('3. Change existing email address')
    print('4. Delete an existing name and email address')

    selection = int(input("Enter a number corresponding to what you'd like to do"))
    data = {}

    if selection == 1:
        name = input('Enter new name')
        data.update(name=name)
        email = input('Enter email address')
        data.update(email=email)
    elif selection == 2:
        # read pickle file
        # pickle_in = open("dict.pickle", "rb")
        data = pickle.load(pickle_in)
        # print(pickle_in)

        find_email = input('Find an email address')
        if 'email' in data:
            print('It matches:', data['email'])
        else:
            print('Sorry, email does not exist.')
    elif selection == 3:
        new_email = input('Change email address')
        data = pickle.load(pickle_in)
        data.update(email = new_email)
        print(data)

    elif selection == 4:
        print('Delete an email address and name')
        print(data)

    print(data)

    # opening file to store the data
    file = open("dict.pickle", "wb")
    pickle.dump(data, file)
    file.close()

    entry = input('Would you like to continue? (enter y/n):')

