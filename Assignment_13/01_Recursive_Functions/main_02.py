def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


n = int(input('Enter an integer number: '))
fact = factorial(n)
print('The factorial of', n, 'is', fact)