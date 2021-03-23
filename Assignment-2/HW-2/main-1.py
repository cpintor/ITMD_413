'''
The current population of the United States is about 328.2 million and that the population
decreases 0.53 percent annually. The current population of Mexico is 127.6 million and
that the population increases 1.06 percent annually. Assume the population percentages
for both countries remain the same, write a program that displays the populations for the
two countries every year until the population of Mexico exceeds that of the United States,
and display the number of years it took.

Name: Cristian Pintor
'''

usPop = 382.2
mxPop = 127.6
year = 2021

while mxPop < usPop:
    usPop -= .53
    mxPop += 1.06
    year += 1
    print("Current year: ", year)
    print("US population exceeds Mexico's at: ", format(usPop, '.2f'))
    print("Mexico's population: ", format(mxPop, '.2f'))

print("In", year, "Mexico exceeds US population at", format(mxPop, '.2f'), "while US population is", format(usPop, '.2f'))
