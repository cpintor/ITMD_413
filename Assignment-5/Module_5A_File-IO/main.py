"""
This program demonstrates Python file/IO
"""

fo = open("data.txt", "w")
fo.write("Python is a great language.\n")
fo.write("This is my next line.")
fo.close() # Closing the file