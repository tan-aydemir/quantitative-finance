#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:46:39 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This Python script examines the mechanics and benefits of two unemotional 
investment strategies that do not rely on historical information. The strategies
are Portfolio Rebalancing & Dollar-Cost Averaging
"""
import pandas as pd

def dollar_cost_average(prices, total_inv=10000, num_purchases=12):
    """
    Create and implement a dollar-cost strategy. This function will process 
    a pd.Series of prices containing historical price data, and returns
    a new pd.DataFrame with a column 'portfolio', which contains the 
    value of a dollar-cost-avereaging portfolio
    """
        
    day_interval1 = round(len(prices) / num_purchases)

    # New DataFrame
    df = pd.DataFrame(index = prices.index)
    # Each payment increase
    inc_inv = total_inv / num_purchases
        
    # Series of Zeros
    zeros = pd.Series(index = prices.index, data = 0)
    #Column for  shares, prices, cash_value, stock_value, portfolio 
    df['Prices'] = prices
    df['shares'] = zeros
    df['cash_value'] = zeros
    df['stock_value'] = zeros
    df['portfolio'] = zeros
    
    count = 0
    idx = 1
    investment = inc_inv
    
    new_price = df['Prices'].iloc[0]
    
    # 
    for i in range(len(prices)):
        if count > day_interval1:
            count = 0
            idx += 1
            investment += inc_inv
            new_price = df['Prices'].iloc[i]
        # Calculate shares
        df['shares'].iloc[i] = investment / new_price    
        #Calculate cash value
        df['cash_value'].iloc[i] = total_inv - investment    
        count = count + 1
    df['stock_value'] = df['shares'] * df['Prices']
    mul_idx = 1   
    every_inv = total_inv / num_purchases  
    count = 0
    for i in range(len(prices)):
        if count > day_interval1:
            mul_idx += 1
            count = 0
        df['portfolio'].iloc[i] = df['stock_value'].iloc[i] + total_inv - (inc_inv * mul_idx)
        # Increase count var. 
        count += 1
        
    # Create a new data frame to store only the Portfolio col
    new_frame = pd.DataFrame(index = prices.index)
    new_frame['portfolio'] = df['portfolio']
        
    return new_frame

def compare_returns(df):
    """
    Create a new DataFrame with the same index as the parameter df, and calculate 
    the periodic market return, strategy return, and abnormal returns.
    Those returns will be stored in the new DataFrame
    """
    # Create new DataFrame
    new_frame = pd.DataFrame(index = df.index)
    new_frame['mkt_ret'] = df['market'].pct_change()
    new_frame['str_ret'] = df['portfolio'].pct_change()
    new_frame['abn_ret'] = new_frame['str_ret'] - new_frame['mkt_ret']
    
    # Display several rows of df
    print("Showing the last several rows of data (values):" )
    print(df.tail())
    
    # Display the descriptive statistics for Returns. 
    print("Descriptive Statistics for Returns")
    print(new_frame.describe())
    
    # Plot Portfolio Values:
    df.plot(title = 'portfolio Values for the Given Asset Prices')
    
    #Plot Cumulaative Returns
    new_frame.cumsum().plot(title = 'Cumulative Returns for the Given Asset Price ')
    
    return new_frame

def create_target_weight_portfolio(prices, target_weights, initial_value = 10000):
    """
    Return a pd.DataFrame with columns containing the values (standardized 
    to $10,000 or the initial_value) of an target-weighted investment in 
    each of the assets in prices, as well as the value of the total portfolio.
    """
    
    print(prices.tail())
    
    # Create a new Data Frame
    df = pd.DataFrame(index = prices.index)
    index = 0   
    df2 = pd.DataFrame(index = prices.index)
    df2['PORTFOLIO']= 0
    
    for key, value in target_weights.items():
        # Find the weight
        w = float(value)
        investment = initial_value * w
        
        compute_portfolio = dollar_cost_average(prices[key], investment, 1)
        df[key] = compute_portfolio
        df2['PORTFOLIO'] += compute_portfolio['portfolio']
    df['portfolio'] = df2['PORTFOLIO']
    return df
        

def plot_relative_weights_over_time(values):
    """
    Create a plot showing the relative weights of each of the 
    assets in a portfolio over time. 
    """
    
    weight_df = pd.DataFrame(index = values.index)
    for col in values.columns:
        if col == 'portfolio':
            break
        
        divided = pd.DataFrame(index = values.index)
        divided[col] = values[col] / values['portfolio']
        weight_df[col] = divided[col]
    
    
    weight_df.plot(title = 'Weight Allocation of Assets Within the Portfolio:')
    
    return weight_df


def create_rebalanced_portfolio(prices, target_weights, rebalance_freq, initial_value=10000):
    """
    Create and return a DaraFrame which consists of portfolio returns when
    the ivestors follows a rebalance apprach
    """
    
    # Compute first investment
    int_inv = {key: initial_value * weight for key, weight in target_weights.items()}
    
    # Compute first shares
    int_share = {key: int_inv[key] / prices[key].iloc[0] for key in prices.columns}
    
    df = pd.DataFrame(index = prices.index, columns = prices.columns)
    
    for company in prices.columns:
        df[company] = prices[company] * int_share[company]
        
    df['portfolio'] = df.sum(axis = 1)
    
    # Iterate over Prices
    for i in range(1, len(prices)):
        if i % rebalance_freq == 0:
            total_val = df.iloc[i].sum() - df['portfolio'].iloc[i]
            new_share = {key: total_val * weight for key, weight in target_weights.items()}
            updated_shares = {key: new_share[key] / prices[key].iloc[i] for key in prices.columns}
            
            for company in prices.columns:
                df[company].iloc[i: ] = updated_shares[company] * prices[company].iloc[i :]
                
        df['portfolio'] = df[prices.columns].sum(axis = 1)
    return df
                

if __name__ == '__main__':
    
    
    df = pd.read_csv('NKE.csv')
    df.index = pd.to_datetime(df['Date'])
    df = pd.DataFrame(df.loc['2017-01-01':'2018-01-01','Adj Close']) 
    
    dfTwo = pd.read_csv('AAPL.csv')
    dfTwo.index = pd.to_datetime(dfTwo['Date'])
    dfTwo = pd.DataFrame(dfTwo.loc['2017-01-01':'2018-01-01','Adj Close']) 


    df.rename(columns={'Adj Close': 'NKE.csv'}, inplace=True)
    df['AAPL.csv'] = dfTwo['Adj Close']
    
    
    target_weights = {'NKE.csv': 0.5, 'AAPL.csv': 0.5}
    b = create_rebalanced_portfolio(df, target_weights, 5, initial_value = 10)
    
    c = create_target_weight_portfolio(df, target_weights, initial_value = 10000)
    
    plot_relative_weights_over_time(c)

    
    print(b.head(50))

    
    
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
