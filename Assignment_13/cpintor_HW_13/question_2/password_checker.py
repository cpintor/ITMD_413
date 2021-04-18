'''
This program  is responsible for checking that the
password meets some pre-defined criteria
Name: Cristian Pintor
'''


def does_password_pass_check(password):
    if len(password) < 9:
        return False
    else:
        print('Good job.')


pw = str(input('Enter password: '))
fact = does_password_pass_check(pw)

print('Idk what Im doing', fact)