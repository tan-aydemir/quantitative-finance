#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:22:08 2024

@author: Tan Aydemir
@email: taydemir@bu.edu

This program has classes for European call and put options
valuation using the Black-Scholes-Merton model.

"""
import math
from scipy.stats import norm

class BSMOption:
    """
    Base Class for Black-Scholes-Merton Option. It encapsulates the data required 
    to do Black-Scholes option pricing formulae. 
    """
    def __init__(self, s, x, t, sigma, rf, div):
        """
        First initialize the BSMOption instance
        """
        self.s = s
        self.x = x
        self.t = t
        self.sigma = sigma
        self.rf = rf
        self.div = div
    
    def __repr__(self):
        """
        Create a nicely-formatted representation of the BSMOption instance.
        """
        newstr = f"s = ${self.s:.2f}, x = ${self.x:.2f}, "
        newstr += f"t = {self.t} (years), sigma = {self.sigma:.3f}, "
        newstr += f"rf = {self.rf:.3f}, div = {self.div}"
        return newstr
    
    def d1(self):
        """
        Compute the first factor -- d1
        """
        numerator = math.log(self.s/self.x) + self.t * (self.rf - self.div + (self.sigma**2)/2)
        denominator = self.sigma * math.sqrt(self.t)
        d1 = numerator/denominator
        return d1
        
    
    def d2(self):
        """
        Compute the second factor -- d2
        """
        d1 = self.d1()
        d2 = d1 - self.sigma * math.sqrt(self.t) 
        return d2
    
    def nd1(self):
        """
        Find cumulative probability density of the factor d1
        """
        nd1 = norm.cdf(self.d1())
        return nd1
        
    def nd2(self):
        """
        Find cumulative probability density of the factor d2
        """
        nd2 = norm.cdf(self.d2())
        return nd2
    
    def value(self):
        """
        Calculate the value for the BSMOption object, which does not exist in this case. 
        """
        print("Cannot calculate value for base class BSMOption.")
        return 0
    
    def delta(self):
        """
        Calculate the delta for the BSMOption object, which does not exist in this case. 
        """
        print("Cannot calculate delta for base class BSMOption.")
        return 0
    
    
    
class BSMEuroCallOption(BSMOption):
    """
    A Child class of the BSMOption class. This class is representing
    a European Call option. 
    """
    def __init__(self, s, x, t, sigma, rf, div):
        """ 
        Initialize BSMEuroCallOption instance.
        """
        super().__init__(s, x, t, sigma, rf, div)
    
    def __repr__(self):
        """
        Create a nicely formatted representation of an BSMEuroCallOption instance
        """
        newstr = f"BSMEuroCallOption, value = ${self.value():.2f}, \n"
        newstr += f"parameters = (s = ${self.s:.2f}, x = ${self.x:.2f}, "
        newstr += f"t = {self.t} (years), sigma = {self.sigma:.3f}, "
        newstr += f"rf = {self.rf:.3f}, div = {self.div})"
        return newstr
    
    def value(self):
        """
        Compute the value of the BSMEuroCallOption instance
        """
        firstPart = self.s * (math.e ** (-1 * self.div * self.t)) * self.nd1()
        secondPart = self.x * (math.e ** (-1 * self.rf * self.t)) * self.nd2()
        return (firstPart - secondPart)
    
    def delta(self):
        """
        Compute the delta of the BSMEuroCallOption instance
        """
        deltaVal = (math.e ** (-self.div * self.t)) * self.nd1()
        return deltaVal
    
    
class BSMEuroPutOption(BSMOption):
    """
    A Child class of the BSMOption class. This class is representing
    a European Put option. 
    """
    def __init__(self, s, x, t, sigma, rf, div):
        """ 
        Initialize BSMEuroPutOption instance.
        """
        super().__init__(s, x, t, sigma, rf, div)
    
    def __repr__(self):
        """
        Create a nicely-formatted representation of an BSMEuroPutOption instance
        """
        newstr = f"BSMEuroPutOption, value = ${self.value():.2f}, \n"
        newstr += f"parameters = (s = ${self.s:.2f}, x = ${self.x:.2f}, "
        newstr += f"t = {self.t} (years), sigma = {self.sigma:.3f}, "
        newstr += f"rf = {self.rf:.3f}, div = {self.div})"
        return newstr
    
    def value(self):
        """
        Compute the value of the BSMEuroPutOption instance
        """
        firstPart = self.x * (math.e ** (-self.rf * self.t)) * (1 - self.nd2())
        secondPart = self.s * (math.e ** (-self.div * self.t)) * (1 - self.nd1())

        return (firstPart - secondPart)
    
    def delta(self):
        """
        Compute the delta of the BSMEuroPutOption instance
        """
        deltaVal = (-math.e ** (-self.div * self.t)) * (1 - self.nd1())
        return deltaVal

if __name__ == '__main__':
    call = BSMEuroCallOption(100, 100, 0.5, 0.25, 0.04, 0.02)
    print(call.delta())
    put = BSMEuroPutOption(100, 100, 0.5, 0.25, 0.04, 0.02)
    print(put.delta())
    call.sigma = 0.5
    print(call.delta())
    put.sigma = 0.5
    print(put.delta())
    
