s = input('Enter 10 numbers separated by a space: ')

items = s.split()
lst = [eval(x) for x in items]

print(lst)