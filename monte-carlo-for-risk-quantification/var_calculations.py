#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:08:41 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

"""
import scipy.stats
import numpy as np
import pandas as pd

def compute_model_var_pct(mu, sigma, x, n):
    """
    Calculate the value at risk as a percent if the asset/portfolio value. 
    """
    z = scipy.stats.norm.ppf(1 - x)
    
    # Calculate the value using the z score
    var = mu * n + z * sigma * (n ** 0.5)
    
    # Return this value
    return var
    
def compute_historical_var_pct(returns, x, n):
    """ 
    Compute the VaR (as a percentage) using the historical simulation approach
    """
    # Compute the risk associated with every single return
    risk_of_returns = np.quantile(returns.dropna(), 1 - x)
    
    # Compute N-day VAR
    n_day_var = risk_of_returns * (n ** 0.5)
    
    # Return the value as a floating point number
    return float(n_day_var)

if __name__ == '__main__':
    df = pd.read_csv('SPY.csv')
    df.index = pd.to_datetime(df['Date'])
    df['returns'] = df['Adj Close'] / df['Adj Close'].shift(1) - 1 
    print(compute_historical_var_pct(df['returns'], 0.98, 5))
    
    

