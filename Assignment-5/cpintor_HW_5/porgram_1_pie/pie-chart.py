"""
This program shows the percentage of employees in each department within a company.
Name: Cristian
"""

import os
import matplotlib.pyplot as plt


def main():
    file = input('Enter the full filename path: ').strip()

    if os.path.isfile(file):
        open_file = open(file, 'r')

        first_line = open_file.readlines()[1:]

        items = []

        for line in first_line:
            split_line = line.split(",")

            num_1 = eval(split_line[1])
            #print(num_1)

            line = open_file.readline()

            items.append(num_1)

        #print(items)
        #print(sum(items))

        dept_percentage = []

        for item in items:
            percentage = (item/(sum(items))) * 100

            #print(percentage)
            dept_percentage.append(percentage)

        print('These are the numbers for each department:',dept_percentage)

        # Creating the pie chart
        items_labels = ['Marketing', 'Information Technology', 'Management', 'Human Resources', 'Finance', 'Supply Chain', 'Manufacturing']
        plt.pie(dept_percentage, labels=items_labels)
        plt.title('Department Name')
        plt.show()


        #print(line)

        open_file.close()
    else:
        print('Did not read file.')


main()
