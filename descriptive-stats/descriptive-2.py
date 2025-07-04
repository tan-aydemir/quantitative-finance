#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 21:32:39 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program processes stock price data and calculates descriptive statistics for the given stocks. 
It makes use of functions from the 'a3task1' module in order to calculate the mean, 
standard deviation, covariance, correlation coefficient, square of the correlation, 
beta, and alpha.

Functions:
- calc_returns(prices): Processes a list of stock prices and calculates the periodic returns.
- process_stock_prices_csv(filename): Reads a data file containing stock price data and returns a list of stock prices.
- stock_descriptive_statistics(filenames): Processes stock prices and displays descriptive statistics about the stocks
    in a formatted fashion

"""
from a3task1 import *

def calc_returns(prices):
    """
    Process a list of stock prices and calculate the periodic 
    returns
    """
    new_list = []
    
    # Calculate the returns using the price values from the list: prices 
    for i in range(1, len(prices)):
        new_list.append((prices[i]/prices[i - 1]) - 1)
    return new_list    

def process_stock_prices_csv(filename):
    """
    Scan a data file containing stock price data, and return a 
    list of stock prices
    """
    new_list = []
    file = open(filename, 'r')
    
    # Read from the filename, disregard the first line, and find
    # adj closing prices
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        if fields[0] == 'Date':
            continue
        price = float(fields[-2])
        new_list.append(price)
    return new_list    

def stock_descriptive_statistics(filenames):
    """
    Process stock prices and display descriptive statistics
    about the stocks
    """
    price_index = process_stock_prices_csv(filenames[0])
    return_index = calc_returns(price_index)
    
    price_list = []
    return_list = []
    
    # Initial lists to store the mean, stdev, covar, correl
    # rsq, beta, alpha numerical values
    means = [mean(return_index)]
    stdev_list = [stdev(return_index)]
    covar_list = [covariance(return_index, return_index)]
    correl_list = [correlation(return_index, return_index)]
    rsq_list = [rsq(return_index, return_index)]
    beta_list = [simple_regression(return_index, return_index)[0]]
    alpha_list = [simple_regression(return_index, return_index)[1]]

    # Traverse through the files and calculate every given value using
    # the calculated returns
    for a in range(1, len(filenames)):
        
        prices = process_stock_prices_csv(filenames[a])
        returns = calc_returns(prices)
        
        means.append(mean(returns))
        stdev_list.append(stdev(returns))
        
        covar_list.append(covariance(return_index, returns))
        correl_list.append(correlation(return_index, returns))
        rsq_list.append(rsq(return_index, returns))
        

        beta_list.append(simple_regression(return_index, returns)[0])
        alpha_list.append(simple_regression(return_index, returns)[1])
    
        formatted_filenames = [[filenames[n][:-3]] for n in range(len(filenames))]

    
    # Create a header list to print out firm abbreviations in a formatted fashion. 
    firstRow = f"{'Symbol: ':<10}" + ' '.join([f'{firm[:-4]:<10}' for firm in filenames])
        
    # Create a table called data to print out the formatted info 
    stats = [
        {'label': 'Mean:', 'values': means},
        {'label': 'StDev:', 'values': stdev_list},
        {'label': 'Covar:', 'values': covar_list},
        {'label': 'Correl:', 'values': correl_list},
        {'label': 'R-SQ:', 'values': rsq_list},
        {'label': 'Beta:', 'values': beta_list},
        {'label': 'Alpha:', 'values': alpha_list}
    ]
    print(firstRow)
    
    # Print the table, formatting each value using 5 decimal places only. 
    for row in stats:
        print(f"{row['label']:8}" + ' '.join([f'{value:10.5f}' for value in row['values']]))

if __name__ == '__main__':
    filenames = ['VTSMX.csv', 'AAPL.csv', 'GOOG.csv'] 
    stock_descriptive_statistics(filenames)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

