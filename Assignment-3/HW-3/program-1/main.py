"""
This program takes the values to be converted from radians to degrees or degrees to radians.

Name: Cristian Pintor
"""
from conversions import *


def main():
    try:
        r = eval(input('Enter the radians to be converted into degrees: '))
        d = eval(input('Enter the degrees to be converted into radians: '))
    except:
        print('Double check your input values please :-)')

    print('The result is', format(radians_to_degrees(r), '.2f'), 'degrees')
    print('The result is', format(degrees_to_radians(d), '.3f'), 'radians')


main()
