#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:20:04 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program encompasses various matrix operations, including creating a matrix, 
swapping its rows, and multiplying its rows by a scalar value. 

Functions: 
    - print_matrix: Takes two parameters, m which is a 2-dimension list 
    (the matrix) and label (a string), and creates a nicely-formatted printout
    
    - zeros: Creates and returns a n*m matrix that contains all zeros
    
    - identity_matrix: Create and return an n * n identity matrix containing 
    the value of 1 along the diagonal.
    
    - transpose: Creates and returns the transpose of the provided matrix
    
    - swap_rows: Performs the elementary row operation that exchanges 
    two rows within the matrix. This function will modify 
    the matrix M such that its row order has changed, 
    but none of the values within the rows have changed.
    
    - mult_row_scalar: Performs the elementary row operation that multiplies
    all values in the row row by the numerical value scalar.
    
    - add_row_into: Performs the elementary-row operation to add the 
    src row into the dest row.
        
"""

def print_matrix(m, label=None):
    """
    Takes two parameters, m which is a 2-dimension list 
    (the matrix) and label (a string), and 
    create a nicely-formatted printout.
    """
    if label == None:
        pass
    else: 
        print(label, "=")
    # Check for the first and last rows/columns to prepare for formatting
    for r in range(len(m)):
        for c in range(len(m[r])):
            # If it's the first element, insert two ['s before
            if r == 0 and c == 0:
                print(f'[[{m[r][c]:.2f}', end=', ')  
                
            # If it's the first element in a separate row, insert 1 [ before
            elif c == 0:
                print(f' [{m[r][c]:.2f}', end=', ')   
            # If it's the last element in the left corner, insert two ]'s after
            elif r == len(m) - 1 and c == len(m[0]) - 1:
                print(f'{m[r][c]:.2f}', end=']] ') 
            elif c == len(m[0]) - 1:
            # If it's the last element of any other row, insert one ] before
                print(f'{m[r][c]:.2f}', end='] ') 
            else:
                print(f'{m[r][c]:.2f}', end=', ')    
        print()

def zeros(n, m = None):
    """ 
    Create and return a n*m matrix that contains all zeros
    """
    # If one parameter is given, create a square 2D list
    if (m == None):
        m = n
    twoDArray = []
    # Assign every element of matrix to 0
    for r in range(n):
        temp = []
        for c in range(m):
            temp.append(0)
        twoDArray.append(temp)
    return(twoDArray)
     
def identity_matrix(n):
    """ 
    Create and return an n * n identity matrix containing 
    the value of 1 along the diagonal.
    """
    twoDArray = zeros(n)
    # Assign the diagonal elements to 1 using a for loop. 
    for i in range(n):
        for j in range(n):
            if (i != j):
                twoDArray[i][j] = 0
            else:
                twoDArray[i][j] = 1
    return twoDArray

def transpose(M):
    """
    Create and return the transpose of the provided matrix
    """
    twoDArray = []

    num_cols = len(M[0])
    num_rows = len(M)
    
    # Traverse through every element, and append to it to the reversed coordinates
    # in a new 2D array
    for i in range(num_cols):
        newArr =[]
        for j in range(num_rows):
            newArr.append(M[j][i])
        twoDArray.append(newArr)
    return twoDArray


def swap_rows(M, src, dest):
    """ 
    Perform the elementary row operation that exchanges 
    two rows within the matrix. This function will modify 
    the matrix M such that its row order has changed, 
    but none of the values within the rows have changed.
    """
    # Print an error if row numbers are not valid. 
    assert ((src >= 0 or src <= len(M)-1) and (dest >= 0 or dest <= len(M)-1)), "Row out of bounds"
    tempArr = M[src]
    M[src] = M[dest]
    M[dest] = tempArr

    
def mult_row_scalar(M, row, scalar):
    """
    Perform the elementary row operation that multiplies
    all values in the row row by the numerical value scalar.
    """
    # Raise exception if the row value are not within range
    if row < 0 or row>len(M):
        raise Exception("Row out of bounds.")
        
    for col in range(len(M[row])):
        M[row][col] = (M[row][col] * scalar)
        
def add_row_into(M, src, dest):
    """
    Perform the elementary-row operation to add the src row into the dest row.
    """
    if src < 0 or src > len(M)-1 or dest < 0 or dest > len(M)-1:
        raise Exception("Row value is out of bounds. ")
    
    #Initialize a temp variable and assign the row values to it. 
    tempRow = M[src]
    for i in range(len(M[dest])):
        M[dest][i] += tempRow[i]
    
        

    

    
    