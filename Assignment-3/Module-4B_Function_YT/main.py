import math

def volume(r):
    # Return the volume of a sphere with radius r
    v = (4.0/3.0) * math.pi * r**3
    return v


volume(3)