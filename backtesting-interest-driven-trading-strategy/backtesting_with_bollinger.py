#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:55:10 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This Python script is a simple Backtesting program.  The objective is to 
test some technical analysis (i.e., charting) trading strategies. In particular, 
it has a variety of functions to analyze some historical asset (e.g., stock) 
prices or other metrics, and create some trading rule based on those metrics

"""
import pandas as pd

def create_bollinger_bands(df, window = 21, no_of_std = 1, column_name = ''):
    """
    Create Bollinger Bands
    """
    # obtain a Series with price data
    if len(column_name) == 0:
        column_name = df.columns[0]
    
    number_of_days = no_of_std
    
    # Compute Rolling Mean
    rolling_mean = df[column_name].rolling(window=window).mean()
    
    # Compute standard deviation of Rolling Mean
    rolling_stdev = df[column_name].rolling(window = window).std()
    
    #Compute upper and lower bounds
    upper_bound = rolling_mean + (number_of_days * rolling_stdev)
    lower_bound = rolling_mean - (number_of_days * rolling_stdev)
    
    #Create a new Pandas DataFrame
    new_df = pd.DataFrame(index=df.index)
    new_df['Observation'] = df[column_name]
    new_df['Rolling Mean'] = rolling_mean
    new_df['Upper Bound'] = upper_bound
    new_df['Lower Bound'] = lower_bound
    
    # Return Data Frame
    return new_df
    

def create_long_short_position(df):
    """
    This function will evaluate the data elements in the Observation
    column against the Bollinger bands in the columns UpperBound and
    LowerBound. The function will apply the long/short strategy. 
    """
    #Create a new Pandas DataFrame
    new_df = pd.Series(index=df.index)
    for i in range(len(df)-1):
        
        # if the price exceeds rolling mean, buy:
        if df['Observation'].iloc[i] > df['Rolling Mean'].iloc[i]:
            
            # requires time travel: must buy on same day that we observe closing price
            #signal.iloc[i] = 1 # buy
            # no time travel required: buy the next day
            new_df.iloc[i+1] = 1 # buy
        else:
            
            # signal.iloc[i] = 0 # no opinion (no return)
            # signal.iloc[i] = -1 # short sell
            new_df.iloc[i+1] = -1 # sell the next day
        
    # store the signal into the DataFrame
    new_frame = pd.DataFrame(index = df.index)
    new_frame['Position'] = new_df
    return new_frame

def calculate_long_short_returns(df, position, column_name = ''):
    """
    Create a plot of the cumulative return for each column in the parameter
    df, a pandas.DataFrame object with one or more series of returns.
    """
    if len(column_name) == 0:
        column_name = df.columns[0]
        
    # Compute the return
    new_frame = pd.DataFrame(index = df.index)
    
    # Compute Market Return
    new_frame['Market Return'] = df[column_name].pct_change()
    
    # Compute Strategy Return
    new_frame['Strategy Return'] = position['Position'].shift(1) * new_frame['Market Return']

    # Compute Abnormal Return
    new_frame['Abnormal Return'] = new_frame['Strategy Return'] - new_frame['Market Return']
    
    return new_frame

def plot_cumulative_returns(df):
    """ 
    Create a plot of the cumulative return for each column in the parameter
    df, a pandas.DataFrame object with one or more series of returns
    """
    # Plot the Cumulative Return
    df.cumsum().plot(title = 'Task 1: Cumulative Return ')
    

if __name__ == '__main__':
    df = pd.read_csv('NKE.csv')
    df.index = pd.to_datetime(df['Date'])
    df = df.loc['2022-03-01':'2022-09-01']
    bb = create_bollinger_bands(df, window = 30, no_of_std = 1, column_name = 'Adj Close')
    position = create_long_short_position(bb)
    returns = calculate_long_short_returns(df, position, 'Adj Close')
    
    returns.plot(title = 'Task 1: Strategy vs. Market Return')
    plot_cumulative_returns(returns)









