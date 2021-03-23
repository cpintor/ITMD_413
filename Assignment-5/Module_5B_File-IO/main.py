"""
This program opens and reads data from a file.
The program will compute each student's test average.
"""
import os


def main():
    file1 = input('Enter a filename full path: ').strip()

    if os.path.isfile(file1):
        infile = open(file1, 'r')
        line = infile.readline()  # Read all content from a file

        # Read line by line using while loop
        while line != '':  # read until end of line
            splitLine = line.split()
            test1 = eval(splitLine[2])  # extract the value of test 1
            test2 = eval(splitLine[3])
            avg = (test1 + test2)/2

            print(splitLine[0], splitLine[1], avg)
            line = infile.readline()  # Read next line from file

        infile.close()
    else:
        print('Failed to open a file')


main()
