#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:59:18 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This Python script aims to find a trading strategy based on the changes in the interest 
rates. It computes the Market Return, Strategy Return and Abnormal Return, 
and plots them on the same grid for comparison. 
"""

import pandas as pd
import matplotlib.pyplot as plt


def create_signal(interest, stock, trading_fee):
    """
    Create a Signal pattern based on the changes in interest rates
    """
    # Find change in interest and add a column to the Interest Data Frame
    interest['Change'] = interest['LT COMPOSITE (>10 Yrs)'].diff()
    
    # A Pandas Series of Zeros
    zero = pd.Series(index = interest.index, data = 0)
    
    #Create a trading fee
    trading = pd.Series(index = interest.index, data = trading_fee)
    interest['Trading Fee'] = trading
    
    # Create a new Pandas Series for the change in interest rate
    change = pd.Series(index = interest.index, data = interest['Change'])
    
    # Create a new Pandas Series to for Signal
    signal = pd.Series(index = stock.index)
    
    # For every value in the Series change
    for i in range(len(change) - 1):
        # If the change in interest rates is positive (rates rose), buy stock
        if interest['Change'].iloc[i] > zero.iloc[i]:
            signal.iloc[i+1] = +1 
        # Else, sell the Stock the following day
        else:
            signal.iloc[i+1] = -1 # sell the following day

    # Store signal numbers in the DataFrame
    new_frame = pd.DataFrame(index = stock.index)
    new_frame['Signal'] = signal
    new_frame['Trading Fee'] = interest['Trading Fee']
    return new_frame

def calculate_returns(signal, stock):
    """
    Calculate the Market, Strategy and Abnormal Returns. Return a Data Frame that
    has all three columns. 
    """
    # Data frame to store the returns
    new_df = pd.DataFrame(index = stock.index)
    
    # Data frame to store the signal & trading fee vals
    signal_df = pd.DataFrame(index = stock.index)
    signal_df['Signal'] = signal['Signal']
    signal_df['Trading Fee'] = signal['Trading Fee']
    
    # Create a Market Return Column
    new_df['Market Return'] = stock['Adj Close'].pct_change()
    
    # Create a Strategy Return Column
    new_df['Strategy Return'] = stock['Adj Close'].pct_change() * signal_df['Signal'] * (1 - signal_df['Trading Fee'])
    
    # Create an Abnormal Return Column
    new_df['Abnormal Return'] = new_df['Strategy Return'] - new_df['Market Return']

    # Return new DataFrame
    return new_df

def plot_cumulative_returns(df):
    """ 
    Create a plot of the cumulative return for each column in the parameter
    df, a pandas.DataFrame object with one or more series of returns
    """
    # Plot Cumulative Returns,
    df.cumsum().plot(title = 'Task 2 -- Cumulative Return of My Strategy vs Market Return ')

if __name__ == '__main__':
    firm = pd.read_csv('WFC_2011.csv')
    firm.index = pd.to_datetime(firm['Date'])
    #firm = firm.loc['2023-06-19':'2023-10-05']
    firm = firm.loc['2023-02-02':'2023-12-29']
    interest_data = pd.read_csv('interest_data.csv') 
    interest_data.index = pd.to_datetime(interest_data['Date'])
    
    #interest_data = interest_data.loc['06/19/23':'10/05/23']
    interest_data = interest_data.loc['02/02/23':'12/29/23']
    interest_data = interest_data.fillna(0)

    # Find the signal data frame and store in a variable. 
    signal_df = create_signal(interest_data, firm, 0.0025)
    
    # Compute the returns and store in a variable
    returns = (calculate_returns(signal_df, firm))
    
    # Plot the Returns
    returns.plot(title = 'Task Two -- Market Returns vs. My Strategy')
    
    # Plot Cumulative Returns,
    plot_cumulative_returns(returns)    
    
    
    
    
    
    
    