'''
This program demonstrates Python if/elif/else statements.
'''

code = input("Type a 2-letter state code that starts with letter C: ")

if code == "CA":
    print("CA is California")
elif code == "CO":
    print("CO is Colodaro")
elif code == "CT":
    print("CT is Connecticut")
else:
    print("Invalid. Please enter a valid state code that starts with letter C.")

print("Thank you.")