#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:34:19 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program implements three methods to create various graphs using
Matplotlib and Pandas. 
"""
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

from a10task2 import *

def plot_stock_prices(symbols):
    """ 
    Create a graph of the historical stock prices for several stocks
    """
    stock_prices = get_stock_prices_from_csv_files(symbols)
    
    # Plot the stock prices. 
    stock_prices.plot()  
    plt.title('stock prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(stock_prices.columns)  

    plt.grid(True)
    plt.show()
        
    
def plot_stock_cumulative_change(symbols):
    """
    Create a graph of the cumulative stock returns for several stocks
    """
    # Get stock prices
    stock_prices = get_stock_prices_from_csv_files(symbols)
    
    # Compute cumulative change
    cumulative_change = stock_prices.apply(lambda x: x / x.iloc[0])
    
    # Plot cumulative change of each stock over time
    for symbol in symbols:
        plt.plot(cumulative_change.index, cumulative_change[symbol], label=symbol)

    plt.title('Cumulative Change in Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Relative Price')
    plt.legend()

    # Edit x-axis for better readability
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))

    plt.show()
    

def plot_efficient_frontier(symbols):
    """
    Create a graph of the efficient frontier (the set of minimum variance portfolios) 
    that can be achieved using a small set of assets. 
    """
    
    # Obtain stock returns and covariance matrix
    returns = get_stock_returns_from_csv_files(symbols)
    cov_matrix = get_covariance_matrix(returns)
    
    meanMatrix = np.matrix(returns.mean())
    covMatrix = np.matrix(cov_matrix)
    
    # Find the global minimum variance portfolio
    w = calc_global_min_variance_portfolio(covMatrix)
    min_variance_return = calc_portfolio_return(meanMatrix, w)
    
    # Create a range of possible returns
    rs = np.linspace(min_variance_return - 0.02, min_variance_return + 0.02)
    
    # Calculate standard deviations of the set of efficient portfolios
    stdevs = calc_efficient_portfolios_stdev(meanMatrix, covMatrix, rs)
    

    plt.plot(stdevs, rs, '-')
    
    # Title and labels
    plt.title('Efficient Frontier')
    plt.xlabel('Portfolio Standard Deviation')
    plt.ylabel('Portfolio Expected Return')
    
    # Display the plot. 
    plt.show()
    
if __name__ == '__main__':
    symbols = ['AAPL',  'DIS', 'GOOG', 'KO', 'WMT']
    plot_stock_prices(symbols)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    