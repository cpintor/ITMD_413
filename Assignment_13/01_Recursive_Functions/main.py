'''This program demonstrates funtion recursive calls'''


def message(times):
    if times > 0:
        print('This is a recursive function')
        message(times - 1)


message(5)