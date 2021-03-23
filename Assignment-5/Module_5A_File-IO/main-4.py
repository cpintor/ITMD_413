"""
This program opens and reads data from a file.
The program will display how many numbers read, sum, and average.
"""
import os


def main():
    file1 = input('Enter a filename full path: ').strip()

    if os.path.isfile(file1):
        infile = open(file1, 'r')
        s = infile.read()  # Read all content from a file

        scores = [eval(x) for x in s.split()]
        print(scores)

        print('There are ', len(scores), 'numbers')
        print('The total is ', sum(scores))
        print('The avg. is ', sum(scores)/len(scores))

        infile.close()
    else:
        print('Failed to open a file')


main()
