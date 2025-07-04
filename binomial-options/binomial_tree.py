#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 10:41:47 2024

@author: Tan Aydemir
@email: taydemir@bu.edu
Description:
    This program implements a binomial tree model for asset price movements. It 
    is designed to simulate the price evolution of an underlying asset over time. 
    The constructor takes in the following parameters: the initial price (s), 
    standard deviation (stdev), risk-free rate (rf), dividend yield (div), 
    total number of years (years), and number of periods (nper). 
    It has several important methods that modify of these parameters 
    to recalculate the tree accordingly. 

"""
import math
from math import e
from a4task1 import print_matrix

class BinomialTree:
    """
    Develops a recombinant binomial tree suitable for any underlying asset
    """

    def __init__(self, s, stdev, rf, div, years, nper):
        """
        Initialize the attributes for the BinomialTree object
        """
        self.s = s
        self.stdev = stdev
        self.rf = rf
        self.div = div
        self.years = years
        self.nper = nper
        self.build_tree()

    def __repr__(self):
        """ 
        Create a beautifully-formatted string representation of
        the BinomialTree instance
        """
        
        newstr = ""
        newstr += "BinomialTree "
        newstr += (
            f"(s={self.s}, stdev={self.stdev}, rf={self.rf}, div={self.div}, "
        )
        newstr += f"t={self.years} years, nper={self.nper}) \n"
        #Iterate over the self.tree variable, and display the appropriate values
        #on the console. 
        for i in range(len(self.tree)):
            for j in range(len(self.tree[i])):
                # If the value is 0, do not display on the console. 
                if self.tree[i][j] != 0:
                    newstr += f"{self.tree[i][j]:8.2f} "
                else:
                    newstr += "         "
            # New line after every row
            newstr += f"\n"
        return newstr

    def build_tree(self):
        """
        Build a binomial tree (as a 2-d list), which will simulate the
        price movements of the s asset
        """
        
        #Calculate h
        h = self.years / self.nper
        #Calculate d
        d = math.e ** ((self.rf - self.div) * h - self.stdev * math.sqrt(h))
        #Calculate u
        u = math.e ** ((self.rf - self.div) * h + self.stdev * math.sqrt(h))
        # Create a zero-matrix to store the newly computated values. 
        zerosMatrix = BinomialTree.zeros(self.nper + 1)
        
        
        price = self.s
        prevPrice = price
        updatedPrice = price    
        
        #Iterate through the zeros matrix. 
        for row in range(len(zerosMatrix)):            
            for col in range(row, len(zerosMatrix[row])):
                # Store the Previous price in the index [row][col]
                zerosMatrix[row][col] = prevPrice
                # Perform the computation PreviousPrice * u to find the node on the right. 
                prevPrice *= u 
            #Perform the computation updatedPrice * d to find the node on the left. 
            updatedPrice = updatedPrice * d
            prevPrice = updatedPrice
        
        #Assign the 2-d list to the self.tree variable.
        self.tree = zerosMatrix
        #return the outcome. 
        return self.tree

    def zeros(num, num2=None):
        """
        Create a zero matrix of size num x num
        """
        if num2 == None:
            num2 = num
        # Create an empty list
        zerosMatrix = []
        for r in range(num):
            temp = []
            for c in range(num2):
                temp.append(0)
            zerosMatrix.append(temp)
        # Return a new Matrix using the 2-D list: zerosMatrix
        return zerosMatrix

    def set_s(self, newVal):
        """
        Modify the initial underlying to be equal to newVal
        """
        assert type(newVal) in {float, int}, "Price must be an integer or a float. "
        self.s = newVal
        self.build_tree()
        
    def set_stdev(self, newVal):
        """
        Set the standard deviation to newVal
        """
        assert type(newVal) in {float, int}, "Standard deviation must be an integer or a float. "
        self.stdev = newVal
        self.build_tree()
        
    def set_nper(self, newVal):
        """
        Set the num of payments to newVal
        """
        assert type(newVal) in {int}, "Periods per year must be an integer value."
        self.nper = newVal
        self.build_tree()

    def set_rf(self, newVal):
        """
        Set the risk-free rate to newVal. 
        """
        assert type(newVal) in {float, int}, "Risk free rate must be an integer or a float. "
        self.rf = newVal
        self.build_tree()
    
    def set_t(self, newVal):
        """
        Set the number of years to newVal
        """
        assert type(newVal) in {float, int}, "Year must be an integer or a float. "
        self.years = newVal
        self.build_tree()
        
    def set_div(self, newVal):
        """
        Set the dividend payment to newVal
        """
        assert type(newVal) in {float, int}, "Dividend payment must be an integer or a float. "
        self.div = newVal
        self.build_tree()

    
if __name__ == "__main__":
    b = BinomialTree (25, 0.25, 0.05, 0.03, 1, 1)
    print(b)
    b.set_s(100)
    b.set_stdev(0.4)
    b.set_nper(5)
    
    b.set_rf(0.03)
    print(b)
    
    
    