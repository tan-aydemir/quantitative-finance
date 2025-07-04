#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:44:22 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program computes the fundamental calculations to find efficient (minimum variance) 
portfolios, as well as the global minimum variance portfolio
"""
import numpy as np
import math
import pandas as pd

def calc_portfolio_return(e, w):
    """
    Calculate and return the portfolio return for a portfolio
    of n >= 2 assets. 
    """
    
    expected = np.dot(e, w.T)
    return float(expected)


def calc_portfolio_stdev(v, w):
    """
    Compute and return the portfolio st dev for a portfolio
    of n >= 2 assets
    """ 
    first = np.dot(w, v)
    second = np.dot(first, w.T)
    
    # Calculate and output the standard deviation as a float
    return float(second) ** 0.5

def calc_global_min_variance_portfolio(v):
    """
    Return the portfolio weights corresponding to the global minimum 
    variance portfolio
    """
    n = len(v)
    
    # Create a column vector of 1s 
    one = np.ones((1, n))
    v_inv = v.I
    c = np.dot(np.dot(one, v_inv), one.T)[0, 0]
    variance = 1 / c
    
    # Compute the weights of the global minimum variance
    minVar = np.dot(np.dot(variance, one), v_inv)
    
    # Convert minimum variance to a NumPy Matrix 
    return np.matrix(minVar)

def calc_min_variance_portfolio(e, v, r):
    """
    Find and return the portfolio weights corresponding to 
    the minimum variance portfolio for the required rate of return r
    """
    n = e.shape[1]
    
    # Create a column vector of 1s
    one = np.ones((1, n))
    
    a = np.dot(np.dot(one, v.I), e.T)
    b = np.dot(np.dot(e, v.I), e.T)
    c = np.dot(np.dot(one, v.I), one.T)
    
    # Convert numpy arrays above to floating point values. 
    a = float(a)
    b = float(b)
    c = float(c)
    
    # Compute A and the value of its determinant. 
    A = np.matrix([[float(b), float(a)], [float(a), float(c)]])
    d = np.linalg.det(A)
    
    g1 = (1/d) * (np.dot(b, one) - a * e)
    g2 = g1 * v.I

    h1 = (1/d) * (c * e - np.dot(a, one))
    h2 = h1 * v.I
    
    wp = g2 + np.dot(h2, r)
    
    # Return the weights of the min variance portfolio as a NumPy Matrix. 
    return np.matrix(wp)


def calc_efficient_portfolios_stdev(e, v, rs):
    """
    Find a series of minimum variance portfolios and returns 
    their standard deviations.
    """
    numberIter = len(rs)
    newArr = []
    
    # Iterate over a set of rate of returns and compute the minimum 
    # variance portfolio for each given rate. 
    for i in rs:
        newArr.append(calc_portfolio_stdev(v, calc_min_variance_portfolio(e, v, i)))
        
    # Output the result as a NumPy array
    return np.array(newArr)


def get_stock_prices_from_csv_files(symbols):    
    """
    Obtain a pandas.DataFrame containing historical stock prices for several stocks
    """
    fn = f"./{symbols[0]}.csv"
    # Read the first filename in the list of symbols
    df = pd.read_csv(fn)
    
    # Create a new index based on the date information in this file. 
    df.index = df['Date']

    prices = pd.DataFrame(index=df.index)
    prices[f'{fn[2:-4]}'] = df['Adj Close']
    
    # for each stock symbol, create the appropriate file name to read:
    for symbol in symbols[1:]:
        fn = f"./{symbol}.csv"
        df = pd.read_csv(fn)
        df.index = df['Date']
        # Append its Adj Close to the dataFrame Prices
        prices[symbol] = df['Adj Close']
    return prices

def get_stock_returns_from_csv_files(symbols):
    """
    Return a single pandas.DataFrame object containing the stock returns
    """
    prices = get_stock_prices_from_csv_files(symbols)
    
    # Get the percent change between current and former prices using
    # the built-in pandas function pct_change(). 
    return prices.pct_change()

def get_covariance_matrix(returns):
    """
    Generate a covariance matrix for the stock returns in returns
    """
    covariance_matrix = returns.cov()
    
    # Return the covariance matrix for the given returns. 
    return covariance_matrix
 

if __name__ == '__main__':
    symbols = ['AAPL',  'DIS', 'GOOG', 'KO', 'WMT']
    returns = get_stock_prices_from_csv_files(symbols)
    print(returns)
    returns2 = get_stock_returns_from_csv_files(symbols)
    print(returns2.head())
    covar = get_covariance_matrix(returns2)
    print(covar)







