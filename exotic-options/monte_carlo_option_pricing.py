#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:28:26 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This Python program implements a hierarchy of option classes, extensible
to many different kinds of options with similar fundamental characteristics 
such as the underlying stock’s mean rate of return and standard deviation of 
retuerns, but with different payoff algorithms. 
"""

from a9task1 import MCStockSimulator
import numpy as np
import math

class MCStockOption(MCStockSimulator):
    """
    This class encapsulates the idea of a Monte Carlo stock option. It inherits
    from the main MCStockOption
    """
    def __init__(self, s, x, t, r, sigma, nper_per_year, num_trials):
        """
        Initialize an MCStockOption instance
        """
        # Call super class
        super().__init__(s, t, r, sigma, nper_per_year)
        
        # Initialize additional variables
        self.num_trials = num_trials
        self.x = x
        self.r = r
        
    def __repr__(self):
        """
        Display a well-formatted version of the MCStockOption object 
        """
        newstr = f"MCStockOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        This method is overridden in the following classes. 
        """
        print("Base class MCStockOption has no concrete implementation of .value().")
        self.mean = np.mean(self.num_trials)
        self.stdev = np.std(self.num_trials)
        return 0

    def stderr(self):
        """
        Return standard error of the option's value
        """
        if 'stdev' in dir(self):
            return self.stdev / math.sqrt(self.num_trials)
        return 0        

class MCEuroCallOption(MCStockOption):
    """
    This class will inherit from MCStockOption class. It refers to European
    Call Options
    """
    def __repr__(self):
        """
        Display a well-formatted version of the MCEuroCallOption object 
        """
        newstr = f"MCEuroCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        Compute the value of the European Call option.
        """
        
        # Generate stock values
        values = self.generate_simulated_stock_values()
        newarr = []
        
        # Iterate for the number of trials
        for i in range(0, self.num_trials): 
            # Get the value of the underlying stock in the last discrete period. 
            lastVal = self.generate_simulated_stock_values()[-1]
            # Calculate the value of the option. 
            optionValue = max((lastVal - self.x), 0) * pow(math.e, (-self.mu * self.t)) 
            newarr.append(optionValue)
        
        # Compute the mean of the Call values
        optionAvg = np.mean(newarr)
        # Compute the mean of the Call values for standard error computation. 
        self.mean = np.mean(newarr)
        # Compute the stdev of the Call values for standard error computation. 
        self.stdev = np.std(newarr)
        return optionAvg
        
class MCEuroPutOption(MCStockOption):
    """
    This class will inherit from MCStockOption class. It refers to European
    Put Options
    """
    def __repr__(self):
        """
        Display a well-formatted version of the MCEuroPutOption object 
        """
        newstr = f"MCEuroPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        Compute the value of the European PUT option.
        """
        values = self.generate_simulated_stock_values()
        newarr = []
        
        # Iterate for the number of trials
        for i in range(0, self.num_trials): 
            # Get the value of the underlying stock in the last discrete period. 
            lastVal = self.generate_simulated_stock_values()[-1]
            # Calculate the value of the option. 
            optionValue = max((self.x - lastVal), 0) * pow(math.e, (-self.mu * self.t)) 
            newarr.append(optionValue)
        # Compute the mean of the PUT values
        optionAvg = np.mean(newarr)
        # Compute the mean of the PUT values for standard error computation. 
        self.mean = np.mean(newarr)
        # Compute the stdev of the PUT values for standard error computation. 
        self.stdev = np.std(newarr)
        return optionAvg
    
   
class MCAsianCallOption(MCStockOption):
    """
    This class will inherit from MCStockOption class. It refers to Asian
    Call Options
    """
    def __repr__(self):
        """
        Display a well-formatted version of the MCAsianCallOption object 
        """
        newstr = f"MCAsianCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        Compute the value of the Asian Call option.
        """
        newarr = []
        # Iterate for the number of trials
        for i in range(0, self.num_trials): 
            # Calculate the value of the Option, using the equation. 
            optionValue = max((np.mean(self.generate_simulated_stock_values())) - self.x, 0) * pow(math.e, (-self.mu * self.t)) 
            newarr.append(optionValue)
        # Calculate the mean of the Call values
        optionAvg = np.mean(newarr)
        # Calculate the mean of the Call values for standard error computation.
        self.mean = np.mean(newarr)
        # Calculate the stdev of the Call values for standard error computation.
        self.stdev = np.std(newarr)
        return optionAvg
    
class MCAsianPutOption(MCStockOption):
    """
    This class will inherit from MCStockOption class. It refers to Asian
    Put Options
    """
    def __repr__(self):
        """
        Display a well-formatted version of the MCAsianPutOption object 
        """
        newstr = f"MCAsianPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        Compute the value of the Asian Put option.
        """
        newarr = []
        # Iterate for the number of trials
        for i in range(0, self.num_trials): 
            # Calculate the value of the Option, using the equation. 
            optionValue = max((self.x - np.mean(self.generate_simulated_stock_values())), 0) * pow(math.e, (-self.mu * self.t)) 
            newarr.append(optionValue)
        # Calculate the mean of the Put values
        optionAvg = np.mean(newarr)
        # Calculate the mean of the Put values for standard error computation.
        self.mean = np.mean(newarr)
        # Calculate the stdev of the Put values for standard error computation.
        self.stdev = np.std(newarr)
        return optionAvg
    
class MCLookbackCallOption(MCStockOption):
    """
    This class will inherit from MCStockOption class. It refers to Look Back
    Call Options
    """
    def __repr__(self):
        """
        Display a well-formatted version of the MCLookbackCallOption object 
        """
        newstr = f"MCLookbackCallOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        Compute the value of the LookBack Call Option
        """
        newarr = []
        # Iterate for the number of trials
        for i in range(0, self.num_trials): 
            # Calculate the value of the Option, using the equation. 
            optionValue = max((np.max(self.generate_simulated_stock_values())) - self.x, 0) * pow(math.e, (-self.mu * self.t)) 
            newarr.append(optionValue)
            
        # Calculate the mean of the Call values
        optionAvg = np.mean(newarr)
        # Calculate the mean of the Put values for standard error computation.
        self.mean = np.mean(newarr)
        # Calculate the stdev of the Call values for standard error computation.
        self.stdev = np.std(newarr)
        return optionAvg
    
class MCLookbackPutOption(MCStockOption):
    """
    This class will inherit from MCStockOption class. It refers to Look Back 
    Put Options
    """
    def __repr__(self):
        """
        Display a well-formatted version of the MCLookbackCallOption object 
        """
        newstr = f"MCLookbackPutOption (s=${self.s:.2f}, x=${self.x:.2f}, t={self.t:.2f} (years), r={self.mu:.2f}, " 
        newstr += f"sigma={self.sigma:.2f}, nper_per_year={self.nper_per_year}, num_trials={self.num_trials})"
        return newstr
    
    def value(self):
        """
        Compute the value of the LookBack Put Option
        """
        newarr = []
        # Iterate for the number of trials
        for i in range(0, self.num_trials): 
            # Calculate the value of the Option, using the equation 
            optionValue = max((self.x - np.min(self.generate_simulated_stock_values())), 0) * pow(math.e, (-self.mu * self.t)) 
            newarr.append(optionValue)
        
        # Calculate the mean of the Put values
        optionAvg = np.mean(newarr)
        # Calculate the mean of the Put values for standard error computation
        self.mean = np.mean(newarr)
        # Calculate the stdev of the Put values for standard error computation
        self.stdev = np.std(newarr)
        return optionAvg
    
    
if __name__ == '__main__':
    pass
    
    
    
    
    
    
    





