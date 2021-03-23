# Replacing a specific part of a string


# Checking for phone number input
import re
pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"1\2\3"  # Groups 1,2 and 3 and concatinating the 3 groups w/o hyphen
user_input = input()
new_user_input = re.sub(pattern, new_pattern, user_input)
print(new_user_input)