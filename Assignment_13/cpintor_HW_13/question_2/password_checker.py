'''
This program is responsible for checking that the
password meets some pre-defined criteria

Name: Cristian Pintor
'''


def does_password_pass_check(password):
    if len(password) == 0:
        return False
    elif password[0].isdigit():
        return True
    else:
        password = password[1:]
        return does_password_pass_check(password)


def main():
    password = input('Please enter a password with at least one digit: ')
    if does_password_pass_check(password):
        print('Nice password!')
    else:
        print('Check your password again')


main()