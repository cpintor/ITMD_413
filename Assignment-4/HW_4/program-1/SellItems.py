"""
This program allows the user to enter any number of
item prices and then calculates the total and applies a 7% sales tax.

Name: Cristian Pintor
"""

# import sys
#
# sys.path.insert(0, '/Users/crissyp/projects/ITMD-413/Assignment-3/HW-3/program-2/calculation.py')
# from calculation import prices

from prices import *

def main():
    input_string = input("Enter product prices: ")
    list = input_string.split()
    sum = 0
    prices(list, sum)

main()

