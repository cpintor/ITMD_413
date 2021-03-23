"""
This program visualizes all of the data gathered from running all of the Python
sort and search algorithms

Name: Cristian Pintor
"""

import matplotlib.pyplot as plt


def bubbleSort():
    bubble_sort = [10000, 30000]
    time = [14.925, 157.359]

    plt.plot(bubble_sort, time)
    plt.xlabel('Total time')
    plt.ylabel('Number sizes')
    plt.title('Bubble Sort Times')

    plt.show()


def shellSort():
    shell_sort = [10000, 30000, 50000, 70000, 90000]
    time = [0.0274, 0.0743, 0.1280, 0.3026, 0.4588]

    plt.plot(shell_sort, time)
    plt.xlabel('Total time')
    plt.ylabel('Number sizes')
    plt.title('Shell Sort Times')

    plt.show()


def quickSort():
    quick_sort = [10000, 30000, 50000, 70000, 90000]
    time = [0.0191, 0.0920, 0.1094, 0.4281, 0.2099, ]

    plt.plot(quick_sort, time)
    plt.xlabel('Total time')
    plt.ylabel('Number sizes')
    plt.title('Quick Sort Times')

    plt.show()


def main():
    # bubble sort
    bubbleSort()

    # shell sort
    shellSort()

    # quick sort
    quickSort()


main()
