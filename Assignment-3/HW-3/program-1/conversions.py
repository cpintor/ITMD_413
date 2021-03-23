"""
This program file contain the conversion functions that will be called to the main program.

Name: Cristian Pintor
"""

import math


def radians_to_degrees(r):
    result = r * (180 / math.pi)
    return result


def degrees_to_radians(d):
    result = d * (math.pi / 180)
    return result
