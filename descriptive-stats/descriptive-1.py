#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:53:43 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program provides functions to calculate various descriptive statistics, 
including mean, variance, standard deviation, covariance, correlation coefficient, 
square of the correlation, and simple linear regression coefficients. 

Functions:
- mean(values): Calculates and returns the mean of the provided values.
- variance(values): Calculates and return the population variance of the values in the list
- stdev(values): Calculates and returns the population standard deviation of the values in the list.
- covariance(x, y): Calculates and returns the population covariance between two lists.
- correlation(x, y): Calculates and returns the correlation coefficient between the two data series.
- rsq(x, y): Calculates and returns the square of the correlation between two data series.
- simple_regression(x, y): Calculates and returns the regression coefficients for a linear regression.

"""

def mean(values):
    """ 
    Calculates and returns the mean of the values provided as parameters
    """
    sum_values = sum(values)
    length_val = len(values)
    mean = sum_values / length_val
    return mean

def variance(values):
    """
    Calculate and return the population variance of the values in the list
    """
    mean_val = mean(values)
    length_val = len(values)
    sum = 0
    # Calculate the sum of squared deviations from the mean with a loop.
    for value in values:
        sum += (value - mean_val)**2
        
    return sum / len(values)

def stdev(values):
    """
    Calculate and return the population standard deviation of the values
    in the list.
    """
    var = variance(values)
    st_dev = (var)**(0.5)
    return st_dev

def covariance(x, y):
    """
    Calculate and return the population covariance for those two lists
    """
    # Print out an error if they are not of the same exact length
    assert len(x)==len(y), "Not the same length."
    mean_x = mean(x) 
    mean_y = mean(y)
    sum = 0
    for a in range(len(y)):
        sum += (x[a] - mean_x) * (y[a] - mean_y)
    return sum / len(y)

def correlation(x, y):
    """
    Calculate and return the correlation coefficient between 
    the data series, x & y
    """
    covar = covariance(x, y)
    stdx = stdev(x)
    stdy = stdev(y)
    return covar / (stdx * stdy)

def rsq(x, y):
    """
    Calculate and return the square of the correlation between 
    the data series, x & y
    """
    corr_x_y = correlation(x, y)
    return corr_x_y**2

def simple_regression(x, y):
    """
    Calculate and return the regression coefficients between these data series
    """
    cov = covariance(x, y)
    var = variance(x)
    
    #Calculate the intercept and coefficient, and merge them in a list. 
    regression_coefficient = cov/(var)
    regression_intercept = mean(y) - (regression_coefficient * mean(x))
    combined_list = [regression_intercept, regression_coefficient]
    return combined_list
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
