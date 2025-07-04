#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:10:18 2024

@author: Tan Aydemir
@email: taydemir@bu.edu
@description: Discounted Cash Flows & Bond Pricing

"""

def cashflow_times(n,m):
    """
    Give the list of times at which a bond makes coupon payments
    """
    total = n * m
    newlist = [number + 1 for number in range(total)]
    return newlist

def discount_factors(r, n, m):
    """
    Calculate and return a list of discount factors for a 
    given annualized interest rate r, for n years, and m discounting periods per year. 
    """
    total = n * m
    # Use list comprehension to calculate discount factors for r, n, and m
    newlist = [(1 / (1 + r / m)**(number + 1)) for number in range(total)]
    return newlist

def bond_cashflows(fv, c, n, m):
    """
    Calculate and return a list if cash flows for some bond specified by 
    the parameters. 
    """
    total_periods = len(cashflow_times(n,m))
    # Use list comprehension to calculate the cash flows for a bond specified
    # by the provided parameters
    coupon = [(c / m) * fv for number in range(total_periods - 1)]
    coupon.append((c / m) * fv + fv)
    return coupon

def bond_price(fv, c, n, m, r):
    """ 
    Calculate and return the price of a bond. 
    """
    arr1 = discount_factors(r, n, m)
    arr2 = bond_cashflows(fv, c, n, m)
    # Use list comprehension to calculate price of a bond. 
    newlist = [arr1[number] * arr2[number] for number in range(n * m)]
    total_pv = sum(newlist)
    return total_pv
    

def bond_yield_to_maturity(fv, c, n, m, price):
    """ 
    Calculate the annualized yield to maturity on some bond.
    """
    dif = price
    accuracy = 0.0001
    
    # Initalize upper and lower bounds
    upper_bound = 1
    lower_bound = 0
    iteration = 0
    
    # Iterate between upper and lower bounds for the bond price until
    # the calculated bond price is close enough to the actual bond price
    while(abs(round(dif, 4)) >= accuracy):
        test_rate = (upper_bound + lower_bound)/2
        pv = bond_price(fv, c, n, m, test_rate)
        dif = price - pv
        if (dif < 0):
            # if the calculated price is too low, try lower rate
            lower_bound = test_rate
        else:
            # else make upper bound lower. 
            upper_bound = test_rate
        iteration = iteration + 1
    return test_rate
    
























 