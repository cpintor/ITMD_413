'''This program demonstrates the concepts of Polymorphism'''


class India(object):
    def capital(self):
        print('The capital of India is New Delhi')

    def language(self):
        print('Hindi is the primary language')


class USA(object):
    def capital(self):
        print('The capital of USA is DC')

    def language(self):
        print('English is the primary language of USA')


# Function that takes any object, capital or language
def func(obj):
    obj.capital()
    obj.language()


# Start of program
lst = []
lst.append(India())
lst.append(USA())

for country in range(0, len(lst)):
    func(lst[country])
    print('\n')