"""
This program demonstrates how to create graphs for data analysis.
"""

import matplotlib.pyplot as plt


def main():
    # create list with the X and Y coordinates of each data point
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # build the line graph
    plt.plot(x_coords, y_coords)

    # add the title
    plt.title('Sample Data')

    # add labels to the axes
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')

    # display the line graph
    plt.show()


# start the program
main()
