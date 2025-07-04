#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:23:34 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program will implement some classes to simulate stock returns and price movements 
(aptask1.py) to assist with pricing path-dependent options (a9task2.py). The first program
consists of a base class to encapsulate the fundamental data members and common calculations 
used to simulate stock returns using Monte Carlo simulation. The second program creates subclasses 
to implement several option pricing algorithms.


"""
import numpy as np
import math
import matplotlib.pyplot as plt

class MCStockSimulator:
    """
    MCStockSimulator encapsulates the data and methods required to simulate stock returns and values. 
    I will also serve as a base class for option pricing. 
    """ 
    def __init__(self, s, t, mu, sigma, nper_per_year):
        """
        Initialize a MCStockSimulator instance. 
        """
        self.s = s
        self.t = t
        self.mu = mu
        self.sigma = sigma
        self.nper_per_year = nper_per_year
        
    def __repr__(self):
        """
        Display the well-formatted MCStockSimulator instance. 
        """
        newstr = f"MCStockSimulator (s=${self.s:.2f}, t={self.t:.2f} (years), mu={self.mu:.2f}, sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year})"
        return newstr
    
    def generate_simulated_stock_returns(self):
        """
        Generate and return a np.array (numpy array) containing a sequence
        of simulated stock returns over the time period t
        """
        
        # Calculate the discrete time period. 
        dt = 1 / self.nper_per_year
        time_periods = int(self.nper_per_year * self.t)
        firstPart = (self.mu - ((self.sigma ** 2) / 2)) * dt 
        
        # Initialize a np array, filling it appropriate values, and the randomly
        # generated Z value.  
        returns_array = firstPart + np.random.normal(size = time_periods) * self.sigma * (dt ** 0.5)
        return returns_array
    
    def generate_simulated_stock_values(self):
        """
        Generate and return a np.array (numpy array) containing a sequence 
        of stock values, corresponding to a random sequence of stock return
        """
        
        # Obtain an array of returns, calling the previous simulated returns function. 
        returns = self.generate_simulated_stock_returns()
        stock_values = np.zeros(len(returns) + 1)
        stock_values[0] = self.s
        
        # Iterate for len(stock_values) number of times, filling each index
        # with its corresponding element. 
        for i in range(1, (len(stock_values))):
            stock_values[i] = stock_values[i-1] * (math.e ** (returns[i-1]))
        return stock_values
    

    
    def plot_simulated_stock_values(self, num_trials = 1):
        """
        Generate a plot of of num_trials series of simulated stock return
        """
        plt.figure(figsize=(10, 6))
        
        # Create a loop to iterate for the number of trials. 
        for _ in range(num_trials):
            
            # Get simulated values
            simulated_values = self.generate_simulated_stock_values()
            # Get time periods
            time_periods = np.linspace(0, self.t, len(simulated_values))
            # Plot the values based on the time periods, and simulated values
            plt.plot(time_periods, simulated_values)
        plt.xlabel('years')
        plt.ylabel('$ value')
        plt.title('Simulated Stock Values')
        plt.grid(True)
        plt.show()
            
    

if __name__ == '__main__':
     sim = MCStockSimulator(100, 2, 0.10, 0.30, 250)
     print(sim.plot_simulated_stock_values(5))
    
    
    
    
    
    