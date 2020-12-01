#!/usr/bin/env python
# coding: utf-8

''' The question is equivalent to calculate the absorbing probabilities of Absorbing Markov chain
more on Absorbing Markov chain:(https://en.wikipedia.org/wiki/Absorbing_Markov_chain) '''

## Google foobar does not support numpy, we would need to define functions to handle matrix calculation

# Reference (Matrix calculation): https://integratedmlai.com/basic-linear-algebra-tools-in-pure-python-without-numpy-or-scipy/
# Reference (Matrix_inverse): https://stackoverflow.com/questions/32114054/matrix-inversion-without-numpy
def zeros_matrix(rows, cols):
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def identity_matrix(n):
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1.0
 
    return IdM

def matrix_subtraction(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
 
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]
 
    return C

def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total
    return C

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


# Absorbing Markov chain have the transition matrix form of P=[[Q,R], [0,I]]
# Calculating absorbing probability require matrix [Q,R]
# Define a swap function to swap row and column of the input into matrix [Q,R]
def swap_matrix(terminal_row, non_terminal_row, non_terminal):
    non_terminal_swap=[]
    for s in non_terminal:
        temp=[]
        for k in non_terminal_row:
            temp.append(s[k])
        for k in terminal_row:
            temp.append(s[k])
        non_terminal_swap.append(temp)
    return non_terminal_swap

# Generate output in the form of [nominator1, nominator2,..., denominator]
def gen_output(B):
    ## Approximate fraction from the numpy array
    solution = []
    for col, j in enumerate(B[0]):
        solution.append(Fraction(B[0][col]).limit_denominator(1000))
    denominator = [i.denominator for i in solution]

    ## Calculate the lcm of denominator and adjust the numerator for output

    lcm = denominator[0]
    for i in denominator[1:]:
        lcm = lcm * i // gcd(lcm, i)
    numerator = [int(i.numerator * lcm / i.denominator) for i in solution]
    output = numerator
    output.append(lcm)

    return output


from fractions import Fraction
# from fractions import gcd # For python 2
from math import gcd # For python 3
def solution(m):
    ## Scale the input into list of probability
    for i, row in enumerate(m):
        sum_row = sum(row)
        for j, col in enumerate(row):
            if m[i][j] != 0:
                m[i][j] = Fraction(m[i][j], sum_row)
    
    ## Split input into terminal and non_terminal list 
    non_terminal_row=[]
    non_terminal=[]
    terminal_row=[]
    for i, row in enumerate(m):
        if i==0 and sum(row)==0:
            return [1,1]
        if sum(row)==0:
            terminal_row.append(i)
        else:
            non_terminal_row.append(i)
            non_terminal.append(row)


    ## Calculate absorbing probabilities
    
    non_terminal_swap=swap_matrix(terminal_row, non_terminal_row, non_terminal)
    Q = [non_terminal_swap[i][:len(non_terminal_swap)] for i in range(len(non_terminal_swap))]
    I=identity_matrix(len(non_terminal_swap))
    R=[non_terminal_swap[i][len(non_terminal_swap):] for i in range(len(non_terminal_swap))]
    C=matrix_subtraction(I, Q)
    B=matrix_multiply(getMatrixInverse(C), R)
    
    return gen_output(B)



solution([
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])


