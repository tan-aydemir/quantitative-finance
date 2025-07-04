#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:06:22 2024

@author: Tan Aydemir
@email: taydemir@bu.edu
@description: Estimating the Change in Bond Price
"""

from a2task1 import *

def bond_duration(fv, c, n, m, r):
    """ 
    Calculate and return the duration metric for the bond. 
    """
    price = bond_price(fv, c, n, m, r)
    cash_flows = bond_cashflows(fv, c, n, m)
    discounted = discount_factors(r, n, m)
    periods = len(cashflow_times(n, m))
    
    # Use list comprehension to calculate the bond's duration metric, starting at time: 1
    bond_d = [((t + 1) * discounted[t] * cash_flows[t] / m) for t in range(periods)]
    return sum(bond_d) / price

def macaulay_duration(fv, c, n, m, price):
    """ 
    Calculate and return the Macaulay duration for the bond
    """
    periods = len(cashflow_times(n, m))
    ytm = bond_yield_to_maturity(fv, c, n, m, price)
    cash_flows = bond_cashflows(fv, c, n, m)
    discounted = discount_factors(ytm, n, m)

    # Use list comprehension to calculate the bond's macaulay duration metric, starting at time: 1
    bond_m = [((t + 1) * discounted[t] * cash_flows[t] / m) for t in range(periods)]
    return sum(bond_m) / price
    
def modified_duration(fv, c, n, m, price):
    """
    Calculate and return the modified duration for the bond. 
    """
    d_mac = macaulay_duration(fv, c, n, m, price)
    ytm = bond_yield_to_maturity(fv, c, n, m, price)
    modified_d = (d_mac) / (1 + ytm / m)
    return modified_d

def bond_convexity(fv, c, n, m, r):
    """
    Calculate and return the convexity metric for the bond. 
    """
    price = bond_price(fv, c, n, m, r)
    cash_flows = bond_cashflows(fv, c, n, m)
    discounted = discount_factors(r, n, m)
    periods = len(cashflow_times(n, m))
    
    # Use list comprehension to calculate the bond's convexity starting at time: 1
    bond_c = [(discounted[t] * (t + 1) * (t + 2) * cash_flows[t]) for t in range(periods)]
    return (sum(bond_c)) / (price * ((m)**2) * (1 + (r / m))**2)

def estimate_change_in_price1(fv, c, n, m, price, dr):
    """
    Calculate and return the estimated dollar change in price that corresponds to 
    a change in the yield 
    """
    change_in_price = (-modified_duration(fv, c, n, m, price)) * price * dr
    return (change_in_price)

def estimate_change_in_price2(fv, c, n, m, price, dr):
    """ 
    Calculate and return the estimated dollar change in price that corresponds to 
    a change in yield
    """
    ytm = bond_yield_to_maturity(fv, c, n, m, price)
    convex = bond_convexity(fv, c, n, m, ytm)
    bond_m = modified_duration(fv, c, n, m, price)
    change_price = price * (((-bond_m) * dr) + ((convex / 2) * (dr**2)))
    
    return change_price














