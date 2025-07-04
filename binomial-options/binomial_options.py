#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:10:37 2024

@author: Tan Aydemir
@email: taydemir@bu.edu
Description: 
    Inheriting from the BinomialTree class in Task 1, the BinomialOption class 
    assists in modeling various types of options, both European and American. 
    It provides additional parameters such as the strike price (x) 
    and time to maturity (t), which is the number of years from the previous Class. 
    It's subclasses include BinomialEuroCallOption, BinomialEuroPutOption, and 
    BinomialAmericanPutOption. These classes provide methods to construct
    option trees and compute their values. 
"""

from a7task1 import *
from a4task1 import print_matrix

class BinomialOption(BinomialTree):
    """
    Create a class named Binomial Option. This is
    a sub-class of BinomialTree from Task 1. 
    """
    def __init__(self, s, x, stdev, rf, div, t, nper):
        """
        Initialize an instance of BinomialOption
        """
        # Call super-class constructor. 
        super().__init__(s, stdev, rf, div, t, nper)
        self.x = x
        self.build_option_tree()


class BinomialEuroCallOption(BinomialOption):
    """ 
    Create a class named BinomialEuroCallOption. This is
    a sub-class of BinomialOption above.
    """
    def __repr__(self):
        """
        Create a beautifully-formatted representation for the
        BinomialEuroCallOption instance. 
        """
        newstr = ""
        newstr += "European Call Option Tree "
        newstr += (
            f"(s={self.s}, x={self.x}, stdev={self.stdev}, rf={self.rf}, div={self.div}, "
        )
        newstr += f"t={self.years} years, nper={self.nper}) \n"
        
        #Iterate over self.option_tree to display its contents on the console. 
        # Only print the values at and above the left diagonal.
        for i in range(len(self.tree[0])):
            for j in range(len(self.tree[i])):
                if (self.option_tree[i][j] != 0):
                    newstr += f"{self.option_tree[i][j]:8.2f} "
                elif (self.option_tree[i][j] == 0 and (i<=j)):
                    newstr += f"{self.option_tree[i][j]:8.2f} "
                else:
                    newstr += "         "
            newstr += f"\n"
        return newstr

    def build_option_tree(self):
        """
        Calculate the option value at each node of the Option tree. 
        Save it as a data attribute 'option_tree.' 
        """
        # Calculate h
        h = self.years / self.nper
        # Calculate d
        d = math.e ** ((self.rf - self.div) * h - self.stdev * math.sqrt(h))
        # Calculate u
        u = math.e ** ((self.rf - self.div) * h + self.stdev * math.sqrt(h))
        # Calculate the probability 'p*'
        pStar = ((math.e ** ((self.rf - self.div) * h)) - d) / (u - d)
        # Initialize a new tree by calling the super-class buid_tree method. 
        newLst = self.build_tree()
        
        # Iterate over every element, beginning from the rightmost col 
        # and going from right to left. 
        for col in range(len(newLst[0]) - 1, -1, -1):
            for row in range(0, col+1):
                if (col == len(newLst[0]) - 1):
                    # If at the rightmost column, 
                    # calculate p and assign it to the current element. 
                    p = max(newLst[row][col] - self.x, 0)
                    newLst[row][col] = p
                else:
                    # Otherwise, use the formula below to compute p 
                    p = (math.exp((-self.rf * h))) * (pStar * newLst[row][col+1] + 
                                                      (1 - pStar) * newLst[row+1][col+1])
                    newLst[row][col] = p
        self.option_tree = newLst
        return self.option_tree

    def set_s(self, newVal):
        """
        Modify the initial underlying to be equal to newVal
        """
        super().set_s(newVal)
        self.build_option_tree()
        
    def set_stdev(self, newVal):
        """
        Set the standard deviation to newVal
        """
        super().set_stdev(newVal)
        self.build_option_tree()
        
    def set_nper(self, newVal):
        """
        Set the number of periods to newVal
        """
        super().set_nper(newVal)
        self.build_option_tree()

    def set_rf(self, newVal):
        """
        Set the risk-freee-rate to newVal
        """
        super().set_rf(newVal)
        self.build_option_tree()
        
    def set_x(self, newVal):
        """
        Set x to newVal
        """
        assert type(newVal) in {float, int}, "X must be an integer of a float. "
        self.x = newVal
        self.build_option_tree()
        
    def set_years(self, newVal):
        """
        Set the duration to newVal
        """
        assert type(newVal) in {float, int}, "Year must be an integer of a float. "
        self.years = newVal
        self.build_option_tree()
        
    def value(self):
        """
        Return the value of the option at Time 0
        """
        return self.option_tree[0][0]
        
    
class BinomialEuroPutOption(BinomialOption):
    """
    Create a class named BinomialEuroPutOption. This is
    a sub-class of the BinomialOption class created before.
    """
    def __repr__(self):
        newstr = ""
        newstr += "European Put Option Tree "
        newstr += (
            f"(s={self.s}, x={self.x}, stdev={self.stdev}, rf={self.rf}, div={self.div}, "
        )
        newstr += f"t={self.years} years, nper={self.nper}) \n"
        
        # Iterate over the elements in self.option_tree. Display them in a
        # diagonal triangle from the leftmost to the rightmost column. 
        for i in range(len(self.tree[0])):
            for j in range(len(self.tree[i])):
                # If at the rigt-most column, use the equation below
                if (self.option_tree[i][j] != 0):
                    newstr += f"{self.option_tree[i][j]:8.2f} "
                # Else if the current element has 0 in it, but its row index
                # is less than the column index, which means it is within 
                # the diagonal triangle, use the equation below. 
                elif (self.option_tree[i][j] == 0 and (i<=j)):
                    newstr += f"{self.option_tree[i][j]:8.2f} "
                else:
                    newstr += "         "
            newstr += f"\n"
        return newstr
            
    def build_option_tree(self):
        """
        Calculate the option value at each node of the Option tree. 
        Save it as a data attribute 'option_tree.' 
        """
        h = self.years / self.nper
        d = math.e ** ((self.rf - self.div) * h - self.stdev * math.sqrt(h))
        u = math.e ** ((self.rf - self.div) * h + self.stdev * math.sqrt(h))
        pStar = ((math.e ** ((self.rf - self.div) * h)) - d) / (u - d)
        newLst = self.build_tree()
        
        # Iterate over the elements in self.tree from the right-most
        # to the left-most column. 
        for col in range(len(newLst[0]) - 1, -1, -1):
            for row in range(0, col+1):
                # If at the right-most column, use the formula below. 
                if (col == len(newLst[0]) - 1):
                    p = max(self.x - newLst[row][col], 0)
                    newLst[row][col] = p
                else:
                    # Else, use the longer formula provided below. 
                    p = (math.exp((-self.rf * h))) * (pStar * newLst[row][col+1] + 
                                                   (1 - pStar) * newLst[row+1][col+1])
                    newLst[row][col] = p
        self.option_tree = newLst
        return self.option_tree
    
            
    def value(self):
        """
        Return the value of the option at Time 0
        """
        return self.option_tree[0][0]
    
class BinomialAmericanPutOption(BinomialOption):
    """
    Create a beautifully-formatted representation for the
    BinomialAmericanPutOption instance. 
    """
    def __repr__(self):
        """
        Create a beautifully-formatted representation for the
        BinomialAmericanPutOption instance. 
        """
        newstr = ""
        newstr += "American Put Option Tree "
        newstr += (
            f"(s={self.s}, x={self.x}, stdev={self.stdev}, rf={self.rf}, div={self.div}, "
        )
        newstr += f"t={self.years} years, nper={self.nper}) \n"
        
        # Iterate over every element in the tree and display them on the console, 
        for i in range(len(self.tree[0])):
            for j in range(len(self.tree[i])):
                # If at the rightmost column, use the formula below
                if (self.option_tree[i][j] != 0):
                    newstr += f"{self.option_tree[i][j]:8.2f} "
                elif (self.option_tree[i][j] == 0 and (i<=j)):
                    newstr += f"{self.option_tree[i][j]:8.2f} "
                else:
                    newstr += "         "
            newstr += f"\n"
        return newstr
    
    def build_option_tree(self):
        """
        Calculate the option value at each node of the Option tree. 
        Save it as a data attribute 'option_tree.' 
        """
        h = self.years / self.nper
        d = math.e ** ((self.rf - self.div) * h - self.stdev * math.sqrt(h))
        u = math.e ** ((self.rf - self.div) * h + self.stdev * math.sqrt(h))
        pStar = ((math.e ** ((self.rf - self.div) * h)) - d) / (u - d)
        newLst = self.build_tree()
        
        # Iterate over the elements in self.tree from the rightmost to the
        # leftmost column. Use the appropriate formulas to compute the value 
        for col in range(len(newLst[0]) - 1, -1, -1):
            for row in range(0, col+1):
                if (col == len(newLst[0]) - 1):
                    p = max(self.x - newLst[row][col], 0)
                    newLst[row][col] = p
                else:
                    p = max(((math.exp((-self.rf * h))) * (pStar * newLst[row][col+1] + 
                                                   (1 - pStar) * newLst[row+1][col+1])), self.x - self.tree[row][col])
                    newLst[row][col] = p
        self.option_tree = newLst
        return self.option_tree
    
    def set_s(self, newVal):
        """
        Modify the initial underlying to be equal to newVal
        """
        super().set_s(newVal)
        self.build_option_tree()
        
    def set_stdev(self, newVal):
        """
        Set the standard deviation to newVal
        """
        super().set_stdev(newVal)
        self.build_option_tree()
        
    def set_nper(self, newVal):
        """
        Set the number of periods to newVal
        """
        super().set_nper(newVal)
        self.build_option_tree()

    def set_rf(self, newVal):
        """
        Set the risk-freee-rate to newVal
        """
        super().set_rf(newVal)
        self.build_option_tree()
        
    def set_x(self, newVal):
        """
        Set x to newVal
        """
        assert type(newVal) in {float, int}, "X must be an integer of a float. "
        self.x = newVal
        self.build_option_tree()
        
    def set_years(self, newVal):
        """
        Set the duration to newVal
        """
        assert type(newVal) in {float, int}, "Year must be an integer of a float. "
        self.years = newVal
        self.build_option_tree()
        
    def set_div(self, newVal):
        """
        Set dividend payment to newVal
        """
        assert type(newVal) in {float, int}, "Dividend must be an integer of a float. "
        self.years = newVal
        self.build_option_tree()
        
    def value(self):
        """
        Return the value of the option at Time 0
        """
        return self.option_tree[0][0]
    
if __name__=='__main__':
    pass
    
    
    
    
    
    
    
    
    
    
    
    
    