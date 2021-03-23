"""
This program shows a company’s profit over the past ten years and displays the
results in a bar graph using Matplotlib.
Name: Cristian Pintor
"""

import os
import matplotlib.pyplot as plt

def main():
    file = input('Enter the full filename path: ').strip()

    if os.path.isfile(file):
        open_file = open(file, 'r')

        first_line = open_file.readlines()[1:]

        years = []
        profit = []

        for line in first_line:
            split_line = line.split(';')

            list_1 = eval(split_line[0])
            # print(list_1)

            line = open_file.readline()

            years.append(list_1)

        for line in first_line:
            split_line_p = line.split('$')

            a = split_line_p

            a = [split_line_p.replace(',', '') for split_line_p in a]



            list_2 = eval(split_line_p[1])
            list_3 = eval(a[1])

            # print(a)
            # print(list_3)

            line = open_file.readline()
            profit.append(list_3)

        print('X-coords: ', years)
        print('Y-coords: ', profit)

        # Creating the bar chart
        x_coords = years
        y_coords = profit

        plt.bar(x_coords, y_coords)
        plt.title('Profits Over Last 10 Years')
        plt.show()


    else:
        print('Did not read file. Try again.')

main()