"""
This program asks the user to enter two 3x3 matrices to be multiplied
and then it gets the result.
Name: Cristian Pintor
"""

matrixA = []
matrixB = []

print('Enter a 3x3 matrix for matrix A: ')

for i in range(9):
    matrixA.append(eval(input()))

print('Enter a 3x3 matrix for matrix B')
for i in range(9):
    matrixB.append(eval(input()))

print('Matrix A: ', matrixA)
print('Matrix B: ', matrixB)

# multiplying
for i in matrixA:
    c_11 = (matrixA[0]*matrixB[0]) + (matrixA[1]*matrixB[3]) + (matrixA[2]*matrixB[6])
    c_21 = (matrixA[3]*matrixB[0]) + (matrixA[4]*matrixB[3]) + (matrixA[5]*matrixB[6])
    c_31 = (matrixA[6]*matrixB[0]) + (matrixA[7]*matrixB[3]) + (matrixA[8]*matrixB[6])

    c_12 = (matrixA[0]*matrixB[1]) + (matrixA[1]*matrixB[4]) + (matrixA[2]*matrixB[7])
    c_22 = (matrixA[3]*matrixB[1]) + (matrixA[4]*matrixB[4]) + (matrixA[5]*matrixB[7])
    c_32 = (matrixA[6]*matrixB[1]) + (matrixA[7]*matrixB[4]) + (matrixA[8]*matrixB[7])

    c_13 = (matrixA[0]*matrixB[2]) + (matrixA[1]*matrixB[5]) + (matrixA[2]*matrixB[8])
    c_23 = (matrixA[3]*matrixB[2]) + (matrixA[4]*matrixB[5]) + (matrixA[5]*matrixB[8])
    c_33 = (matrixA[6]*matrixB[2]) + (matrixA[7]*matrixB[5]) + (matrixA[8]*matrixB[8])

print('The multiplication of the matrices is: ')
print(format(c_11, ',.1f'), format(c_12, ',.1f'), format(c_13, ',.1f'))
print(format(c_21, ',.1f'), format(c_22, ',.1f'), format(c_23, ',.1f'))
print(format(c_31, ',.1f'), format(c_32, ',.1f'), format(c_33, ',.1f'))