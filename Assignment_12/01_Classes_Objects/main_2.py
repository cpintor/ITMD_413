import datetime


# Classes and methods
class User:
    # Docstring
    """
    Storing name and birthday
    """
    # Creating an __init__ method
    def __init__(self, full_name, birthday):
        # self.[field name]=[value]
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last names
        name_pieces = full_name.split(' ')
        # first string in array
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    # This method returns age of user in years
    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2001, 5, 12)
        # Extracting year, month, day
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        # Date object for user's birthday
        dob = datetime.date(yyyy, mm, dd)
        # Getting age
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


# user = User('Dave Bowman', '19731123')
# print(user.name)
# print(user.first_name)
# print(user.last_name)
# print(user.birthday)
#
# # Displaying overview of User class
# help(User)

user = User('Dave Bowman', '19710315')
print(user.age())