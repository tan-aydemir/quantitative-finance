#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:03:21 2024

@author: Tan
@email: taydemir@bu.edu

This program uses Numpy to perform multiple linear algebra calculations on
bond analytics and pricing. 
"""

import numpy as np

def bond_price(times, cashflows, rate):
    """ 
    Calculate and return the price of a bond, given it’s series of cashflows
    and discount rate
    """
    numPeriods = len(times)
    timesMatrix = np.matrix([times])
    
    # Transform cashflows to a NumPy Matrix
    cashflows = np.matrix([cashflows])
    
    # Calculate the bond price using the formula for present value
    # of cash flows discounted at the given rate
    d = [1 / ((1 + rate) ** t) for t in times]
    d = np.matrix([d])
    p = d * cashflows.T
    
    #Return the value as a float
    return float(p)

def bootstrap(cashflows, prices):
    """
    Implement the bootstrap method. Return the matrix of implied discount factors
    """

    # Convert the prices and cashflows into NumPy matrices. 
    cashflows = np.matrix(cashflows)
    prices = np.matrix(prices)
    
    # Compute the implied Discount Rate. 
    d = cashflows.I * prices.T
    return d

def bond_duration(times, cashflows, rate):
    """
    Calculate and return the duration metric for a bond.
    """
    
    # Compute price of bond via using the existing bond_price method. 
    priceOfBond = bond_price(times, cashflows, rate)
    
    # Compute discount factors
    discountFactors =  [1 / ((1 + rate) ** t) for t in times]
    discountFactors = np.array(discountFactors)
    
    # Convert the cash flows into a NumPy Array
    cashflows = np.array(cashflows)
    
    # Calculate total periods of time. 
    times = np.array(times)
    bond_duration = (1 / priceOfBond) * times * cashflows 
    bond_duration = np.dot(bond_duration, discountFactors.T)
    
    # Return bond duration as a floating point value. 
    return float(bond_duration)


if __name__ == '__main__':
    times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cashflows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]
    print(bond_duration(times, cashflows, 0.035))
    
    
    
    
    
    
    
    
    
    
    
    
    