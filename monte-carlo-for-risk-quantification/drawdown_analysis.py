#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:30:53 2024

@author: Tan Aydemi
@email: taydemir@bu.edu
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from a9task1 import MCStockSimulator


def compute_drawdown(prices):
    """
    Process a column of asset prices
    """
    
    # Create a new Pandas data frame, and set its data to prices
    df = pd.DataFrame(data = prices)
    # Assign it an index that is also the index of pthe column prices
    df.index = prices.index
    
    # Rename Adjusted Close col name to price
    df = df.rename(columns = {'Adj Close': 'prices'})
    df['prev_max'] = df.cummax()
    df['dd_dollars'] = abs(df['prices'] - df['prev_max'])
    df['dd_pct'] = df['dd_dollars'] / df['prev_max']
    return df
    
def plot_drawdown(df):
    """
    Create and show two charts:
        1 - The historical price and previous maximum price
        2 - The drawdown since previous maximum price as a percentage lost
    """
    
    # Plot the first graph (prices vs prev_max together)
    selected_column = df[['prices', 'prev_max']]
    selected_column.plot()
    plt.title('Prices and Previous Maximum')
    
    # Show plot
    plt.show()
    
    # Plot the second graph (drawdown percent with date on the x axis.)
    selected_column2 = df['dd_pct']
    selected_column2.plot()
    plt.title('Drawdown Percentage')  
    
    # Show plot
    plt.show()

def run_mc_drawdown_trials(init_price, years, r, sigma, trial_size, num_trials):
    """
    Use the Monte Carlo Stock simulation to to simulate the
    price path evolution of a stock
    """
    
    # Create a np.array
    max_drawdowns = np.zeros(num_trials)
    
    for i in range(num_trials):
        sim = MCStockSimulator(init_price, years, r, sigma, trial_size)
        price_list = sim.generate_simulated_stock_values()

        # Calculate the drawdown for each trial
        drawdowns = (price_list - np.maximum.accumulate(price_list)) / price_list
        
        # Compute the absolute value of the drawdowns for formatting
        drawdowns = abs(drawdowns)
        
        # Obtain the max drawdown from the array
        max_drawdowns[i] = np.max(drawdowns)

    # Create and return the resulting array as a Pandas Series
    return pd.Series(max_drawdowns)


if __name__ == '__main__':
    df = pd.read_csv('SPY.csv')
    df['ret'] = np.log(df['Adj Close'] / df['Adj Close'].shift(1))    
    trial_size = 252
    init_price = float(df['Adj Close'].sample())
    r = df['ret'].mean() * trial_size
    sigma = df['ret'].std() * np.sqrt(trial_size)
    years = 10
    num_trials = 100
    max_dd = run_mc_drawdown_trials(init_price,  years, r, sigma, trial_size, num_trials)
    print(max_dd.describe())
    max_dd.hist()
