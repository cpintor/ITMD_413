"""
This program demonstrates how to create graphs for data analysis.
"""

import matplotlib.pyplot as plt


def main():
    # Create a list of sales amount
    sales = [100,200,300,600]

    # Create a list of labels for the slices
    slice_labels = ['1st Q','2nd Q','3rd Q','4th Q']

    # Create a pie chart from the values that we have above
    plt.pie(sales, labels=slice_labels)

    # Add title
    plt.title('Sales by Quarter')

    # display the line graph
    plt.show()


# start the program
main()
