#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:02:14 2024

@author: Tan Aydemir
@email: taydemi@bu.edu

This Pythion script works with 5 distinct stock prices, and creates 4 different
portfolios: (Equal weights with rebalancing, equal weights without rebalancing, 
efficient mean variance with rebalancing and efficient mean variance without rebalancing)

It uses risk measurement techniques including 10-day-value at risk as well as
Maximum drawdown. Finally, the program plots the cumulative returns of those portfolios
"""

import numpy as np
import pandas as pd
import math

from a13task1 import *  

def begin():
    """
    Start the Program -- this function creates 5 different stock csv files
    and creates a single data frame that includes each of their price values
    """
    s1 = pd.read_csv('INTC.csv')
    s1.index = pd.to_datetime(s1['Date'])
    
    # Alhpabet Stock
    s2 = pd.read_csv('GOOG.csv')
    s2.index = pd.to_datetime(s2['Date'])
    
    # Microsoft Stock
    s3 = pd.read_csv('MSFT.csv')
    s3.index = pd.to_datetime(s3['Date'])
    
    # Cadence Systems Stock
    s4 = pd.read_csv('CDNS.csv')
    s4.index = pd.to_datetime(s4['Date'])
    
    # NVIDIA Stock
    s5 = pd.read_csv('NVDA.csv')
    s5.index = pd.to_datetime(s5['Date'])
    
    df = pd.DataFrame(index = s1.index) # slice some rows
    df['INTC'] = s1['Adj Close']
    df['GOOG'] = s2['Adj Close']
    df['MSFT'] = s3['Adj Close']
    df['CDNS'] = s4['Adj Close']
    df['NVDA'] = s5['Adj Close']

    return df


# PORTFOLIO 1: Equal weights, without rebalancing
def calculate_equal_weight_without_rebalance(stockPrices, weight, initial_value):
    """
    Find an equally weighted portfolio of the given stock prices, without re-balancing.
    """
    #Create a dictonary to store the weights
    target_weights = {}
    for a in stockPrices.columns:
        target_weights[a] = weight
    
    # Call create_target_weight_portfolio method. A default inv of 10K
    getPortfolioTarget = create_target_weight_portfolio(stockPrices, target_weights, initial_value)
    # Compute portfolio return
    returnPortfolio = pd.DataFrame(index = stockPrices.index)
    returnPortfolio['Returns'] = getPortfolioTarget['portfolio'].pct_change()
        
    return returnPortfolio


# PORTFOLIO 2: Equal weights, without rebalancing
def calculate_equal_weight_with_rebalance(stockPrices, weight, rebalance_freq, initial_value):
    """
    Find an equally weighted portfolio of the given stock prices, with re-balancing.
    """
    # Create a dictionary to store target_weights
    target_weights = {}
    
    for a in stockPrices.columns:
        target_weights[a] = weight
      
    # Obtain Rebalanced Portfolio
    getPortfolioTarget = create_rebalanced_portfolio(stockPrices, target_weights, rebalance_freq, initial_value)
    
    #Create a data frame for returns
    returnPortfolio = pd.DataFrame(index = stockPrices.index)
    # Get Portfolio return
    returnPortfolio['Returns'] = getPortfolioTarget['portfolio'].pct_change()
    
    return returnPortfolio

#PORTFOLIO 3: Mean-Var Efficient Portfolio, with rebalancing
def calculate_mean_var_portfolio_without_rebalance(stockPrices, weight, initial_value):
    """
    Calculate weights for a portfolio that matches a target return with minimum variance.
    """
    
    #Create a dictonary to store the weights
    target_weights = {}
    for a in stockPrices.columns:
        target_weights[a] = weight
    
    # Call create_target_weight_portfolio method. A default inv of 10K
    getPortfolioTarget = create_target_weight_portfolio(stockPrices, target_weights, initial_value)

    # Separaete the portfolio from the data frame
    onlyPortfolio = pd.DataFrame(index = stockPrices.index)
    onlyPortfolio['portfolio'] = getPortfolioTarget['Portfolio']
    
    
    # Get rid of the portfolio values colum in getPortfolioTarget
    getPortfolioTarget = getPortfolioTarget.drop('portfolio', axis = 1)

    # Compute Portfolio Returns
    assetReturns = getPortfolioTarget.pct_change()
    
    cov_matrix = assetReturns.cov() * 252
    mean_returns = assetReturns.mean() * 252
    
    n = len(mean_returns)
    
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    ones = np.ones(n)
    A = ones.T @ inv_cov_matrix @ mean_returns
    B = mean_returns.T @ inv_cov_matrix @ mean_returns
    C = ones.T @ inv_cov_matrix @ ones

    determinant = B * C - A ** 2
    f = 1 / determinant

    g = (f * ((B * ones - A * mean_returns) @ inv_cov_matrix))
    h = (f * ((C * mean_returns - A * ones) @ inv_cov_matrix))

    # Compute target return
    target_return = onlyPortfolio['portfolio'].pct_change().mean()
    
    # Get the new weights
    weights = g + h * target_return
    
    # Get the new portfolio return values
    target_weights = {}
    index = 0
    for i in stockPrices.columns:
        target_weights[i] = weights[index]
        index += 1
    
    print("HEY THIS:", target_weights)
    getPortfolioTarget = create_target_weight_portfolio(stockPrices, target_weights, initial_value)
    returnPortfolio = pd.DataFrame(index = stockPrices.index)
    returnPortfolio['Returns'] = getPortfolioTarget['portfolio'].pct_change()
    return returnPortfolio

# PORTFOLIO 4: Mean-Var Efficient Portfolio, with rebalancing
def calculate_mean_var_portfolio_with_rebalance(stockPrices, weight, rebalance_freq, initial_value):
    """
    Calculate weights for a portfolio that matches a target return with minimum variance.
    """
    
    #Create a dictonary to store the weights
    target_weights = {}
    for a in stockPrices.columns:
        target_weights[a] = weight
    
    # Call create_target_weight_portfolio method. A default inv of 10K
    getPortfolioTarget = create_rebalanced_portfolio(stockPrices, target_weights, rebalance_freq, initial_value)

    # Separaete the portfolio from the data frame
    onlyPortfolio = pd.DataFrame(index = stockPrices.index)
    onlyPortfolio['portfolio'] = getPortfolioTarget['portfolio']
    
    
    # Get rid of the portfolio values colum in getPortfolioTarget
    getPortfolioTarget = getPortfolioTarget.drop('portfolio', axis = 1)

    # Compute Portfolio Returns
    assetReturns = getPortfolioTarget.pct_change()
    
    cov_matrix = assetReturns.cov() * 252
    mean_returns = assetReturns.mean() * 252
    
    n = len(mean_returns)
    
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    ones = np.ones(n)
    
    # Compute A B and C
    A = ones.T @ inv_cov_matrix @ mean_returns
    B = mean_returns.T @ inv_cov_matrix @ mean_returns
    C = ones.T @ inv_cov_matrix @ ones

    # Compute the determinant
    determinant = B * C - A ** 2
    f = 1 / determinant

    g = (f * ((B * ones - A * mean_returns) @ inv_cov_matrix))
    h = (f * ((C * mean_returns - A * ones) @ inv_cov_matrix))

    # Compute target return
    target_return = onlyPortfolio['portfolio'].pct_change().mean()
    
    # Get the new weights
    weights = g + h * target_return
    
    # Get the new portfolio return values
    target_weights = {}
    index = 0
    for i in stockPrices.columns:
        target_weights[i] = weights[index]
        index += 1
    
    getPortfolioTarget = create_rebalanced_portfolio(stockPrices, target_weights, rebalance_freq, initial_value)
    returnPortfolio = pd.DataFrame(index = stockPrices.index)
    returnPortfolio['Returns'] = getPortfolioTarget['portfolio'].pct_change()
    return returnPortfolio


def calculate_10_day_var(stockPrices, weight, initial_value):
    """
    Compute the 10-Day VaR (Value at Risk)
    """
    returns = calculate_equal_weight_without_rebalance(stockPrices, weight, initial_value)
    
    daily_mean_return = returns['Returns'].mean()
    std_dev_returns = returns['Returns'].std()
    n = 10
    
    # Z score is 2.326 for a 98% confidence interval
    z = 2.326
    
    # Compute 10-Day-Var
    var_ten_day = float(daily_mean_return) * n + z * std_dev_returns * (n**0.5)
    return var_ten_day


def compute_drawdown(stockPrices, weight, rebalance_freq, initial_value):
    """
    Compute Max Drawdown
    """
    target_weights = {}
    
    # Create target weights
    for a in stockPrices.columns:
        target_weights[a] = weight
        
    getPortfolioTarget = create_target_weight_portfolio(stockPrices, target_weights, initial_value)
    
    # Create a new Pandas data frame, and set its data to prices
    df = pd.DataFrame(index = stockPrices.index, data = getPortfolioTarget['portfolio'])
    
    # Rename Adjusted Close col name to price
    df = df.rename(columns = {'portfolio': 'prices'})
    df['prev_max'] = df.cummax()
    df['dd_dollars'] = abs(df['prices'] - df['prev_max'])
    df['dd_pct'] = df['dd_dollars'] / df['prev_max']
    
    #Compute Max Drawdown
    max_drawdown_amount = df['dd_dollars'].max()
    return max_drawdown_amount


def plot_portfolio_returns(stockPrices, weight, rebalance_freq, initial_value):
    """
    Plot the cumulative portfolio returns for the 4 different portfolios
    """
    equal_rebalance = calculate_equal_weight_with_rebalance(stockPrices, weight, rebalance_freq, initial_value)
    equal_without_rebalance = calculate_equal_weight_without_rebalance(stockPrices, weight, initial_value)
    mean_var_without_rebalancing = calculate_mean_var_portfolio_without_rebalance(stockPrices, weight, initial_value)
    mean_var_rebalancing = calculate_mean_var_portfolio_with_rebalance(stockPrices, weight, rebalance_freq, initial_value)
    
    # Create empty dataFrame
    combined_returns = pd.DataFrame(index = equal_rebalance.index)
    combined_returns['Equal Weighted (No Rebalancing)'] = equal_without_rebalance['Returns']
    combined_returns['Equal Weighted (With Rebalancing)'] = equal_rebalance['Returns']
    combined_returns['Mean Var Portfolio (Without Rebalancing)'] = mean_var_without_rebalancing['Returns']
    combined_returns['Mean Var Portfolio (With Rebalancing)'] = mean_var_rebalancing['Returns']

    
    # Plot combined returns
    combined_returns.cumsum().plot(title = 'Comparing Various Cumulative Portfolio Returns')



if __name__ == '__main__':
    
    # Initialize and create a data frame with stock prices in columns
    listOfPrices = begin()
    
    # Find an equally wieghted portfolio without rebalancing 
    portfolio_equal_without_rebalancing = calculate_equal_weight_without_rebalance(listOfPrices, 1/(len(listOfPrices.columns)), 1000)
    calculate_ten_day_var = calculate_10_day_var(listOfPrices, 1/(len(listOfPrices.columns)), 1000)
    x = compute_drawdown(listOfPrices, 1/(len(listOfPrices.columns)), 20, 1000)

    # Find an equally weighted portfolio with rebalancing (every 20 days)
    portfolio_equal_with_rebalancing = calculate_equal_weight_with_rebalance(listOfPrices, 1/len(listOfPrices.columns), 20, 1000)
    calculate_ten_day_var = calculate_10_day_var(listOfPrices, 1/(len(listOfPrices.columns)), 1000)
    x = compute_drawdown(listOfPrices, 1/(len(listOfPrices.columns)), 20, 1000)

    # Find a mean_variance_portfolio without rebalancing
    returns = calculate_mean_var_portfolio_without_rebalance(listOfPrices, 1/len(listOfPrices.columns), 1000)


    # Find a mean_variance portfolio with rebalancing (every 20 days)
        
    plot_portfolio_returns(listOfPrices, 1/len(listOfPrices.columns), 20, 1000)


    