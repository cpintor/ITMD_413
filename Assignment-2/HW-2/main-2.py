'''
Observe the Troubleshooting Chart for Diesel Engine below. Write a program based on the given
chart. Make sure your program validates the input data. For example, value 50x is invalid, it
should be 50.

Name: Cristian Pintor
'''

print("Check status lights, enter color e.g. Green, Amber or Red: ")
color = input("Enter a color value: ")

try:
    if color == 'Green':
        print("Do restart procedure")
    elif color == 'Amber':
        print("Check fuel line service")
    elif color == 'Red':
        print("Shut-off all input lines. Check meter #3.")
        meter = int(input("Enter meter value: "))
        if meter >= 50:
            print("Measure flow velocity at iniet 2-B.")
            flowInput = input("Enter 'High', 'Low' or 'Normal': ")
            if flowInput == 'High' or flowInput == 'Low':
                print("Refer unit for factory service.")
            elif flowInput == 'Normal':
                print("Refer to iniet service manual.")
        else:
            print("Check main line for test pressure.")
            flowInput = input("Enter 'High', 'Low' or 'Normal': ")
            if flowInput == 'High' or flowInput == 'Low':
                print("Refer to main line manual.")
            elif flowInput == 'Normal':
                print("Refer to motor service manual.")
except:
    print("Error, check value and try again")
