"""This program demonstrates function overloading"""


class Human:
    def greeting(self, name=None):
        if name is not None:
            print('hello ' + name)
        else:
            print('Hello')



# start the program
obj = Human()
obj.greeting()
obj.greeting('Eric')