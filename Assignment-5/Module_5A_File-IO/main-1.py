filename = input('Enter the filename full path: ')
print('The filename you have entered is', filename)

file1 = open(filename, 'w')
radius = 1.5
area = radius * 3.1415 * 3.1415

file1.write('With radius = %.2f, the area = %.2f' % (radius, area))

file1.close()
