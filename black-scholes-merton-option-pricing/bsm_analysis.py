#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:24:05 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program calculates option values and implied volatility for European call
and put options using the BSM model.

"""

from a8task1 import *

def generate_option_value_table(s, x, t, sigma, rf, div): 
    """
    Print a well-formatted table which will demonstrate the change in option 
    prices based on a change in the price of the underlying stock
    """
    
    # New European Call instance
    callObject = BSMEuroCallOption(s, x, t, sigma, rf, div)
    
    #New European Put instance
    putObject = BSMEuroPutOption(s, x, t, sigma, rf, div)
    
    upperLimit = callObject.s + 10 
    lowerLimit = callObject.s - 10
    
    print(callObject)
    print(putObject)
    print()
    print("Change in option values w.r.t. change in stock price: ")
    
    print("      price      call value  put value   call delta  put delta")
    
    # Iterate through a range of prices from -10 to + 10 of the actual price. 
    for i in range(lowerLimit, upperLimit + 1):
        
        # First, set the price to i
        callObject.s = i
        putObject.s = i
        
        # Call the value() function to get the value of Call & Put Options
        callValue = callObject.value()
        putValue = putObject.value()
        
        # Call the delta() function to get the delta of Call & Put Options
        callDelta = callObject.delta()
        putDelta = putObject.delta()
        
        # Print the values in a formatted way.  
        print(f"${callObject.s:12.2f}{callValue:12.4f}{putValue:12.4f}{callDelta:12.4f}{putDelta:12.4f}")


def calculate_implied_volatility(option, value):
    """
    Compute the implied volatility of an option. 
    """
    accuracy = 0.00001
    dif = value

    upperBound = 1
    lowerBound = 0
    testRate = (upperBound + lowerBound) / 2

    # Change the test_rate consistently until the accuracy is achieved
    while True:
        option.sigma = testRate # Set the stdev of option to testRate
        optionValue = option.value() # Calculate the optionValue using the new test rate
        dif = value - optionValue
        
        # If the difference is better than our provided accuracy index, exit the loop. 
        if abs(dif) < accuracy:
            break
        
        # If the difference is less than 0 assign upperBound to testRate
        if dif < 0:
            upperBound = testRate
        
        #If the difference is greater than 0 assign lowerBound to testRate
        else:
            lowerBound = testRate
        testRate = (upperBound + lowerBound) / 2
    
    # Return test rate
    return testRate

        
if __name__ == '__main__':
    call = BSMEuroCallOption(100, 100, 0.5, 0.25, 0.04, 0.02)
    put = BSMEuroPutOption(100, 100, 0.5, 0.25, 0.04, 0.02)
    generate_option_value_table(90, 95, 1.25, 0.3, 0.05, 0.02)