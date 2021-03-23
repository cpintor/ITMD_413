"""
This program demonstrates how to create graphs for data analysis.
"""

import matplotlib.pyplot as plt


def main():
    # Create x-axis values
    x = [5, 3, 7, 2, 6]

    # Create y-axis values
    y = [10, 2, 4, 7, 7]

    # Plot the bar chart
    plt.bar(x,y)

    # Add title
    plt.title('Sales')

    # display the line graph
    plt.show()


# start the program
main()
