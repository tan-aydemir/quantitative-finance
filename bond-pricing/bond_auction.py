#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 14:02:35 2024

@author: Tan Aydemir
@email: taydemir@bu.edu
@description: Simulating a Bond Auction
"""

from a2task1 import *

def collect_bids(filename):
    """
    Process the data file containing the bids. 
    """
    my_list = []
    file = open(filename, 'r')
    # Iterate over every line in each file
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        if (fields[0] == 'bid_id'):
            # Disregard the first line in every file
            continue
        bid_id = int(fields[0])
        bid_amount = int(fields[1])
        bid_price = float(fields[2])
        my_list.append([bid_id, bid_amount, bid_price])
    return my_list

def print_bids(bids):
    """
    Produce a beautifully-formatted table of the bids. 
    """
    print(f"Bid ID{'':8}Bid Amount{'':8}Price")
    # Iterate over each bid
    for bid in bids:
        bid_id = bid[0]
        bid_amount = bid[1]
        price = bid[2]
        print(f"{bid_id}{'':12}${bid_amount:8}{'':8}${price:8.3f}")
        

    
def find_winning_bids(bids, total_offering_fv, c, n, m):
    """
    Process a list of bids and Determine which are successful in this auction
    """
    # sort the bids by bid_price (in descending order), followed by bid_amount (in descending order)
    sortedBids = sorted(bids, key=lambda x: (x[2], x[1]), reverse=True) 
    print()
    print("Here are all of the bids, sorted by price descending: ")
    print_bids(sortedBids)
    print()
    total_offering = float(total_offering_fv)
    print(f"The auction is for ${total_offering:.2f} of bonds")
    print()
    
    count = 0
    # Set price to the first value for price in the sorted table. 
    price = sortedBids[0][2]
    # Iterate over the sorted bids
    for bid in sortedBids:
        # If the total amount of bonds being sold is 0 set bid_amount to 0 for remaining bids. 
        if (total_offering_fv == 0):
            bid[1] = 0
        else:
            # If bid_amount is larger than the remaining total amount of bonds, set bid_amount to
            # the remaining total amount of bonds. Then set the total amount of bonds to 0
            if (bid[1] > total_offering_fv):
                bid[1] = total_offering_fv
                total_offering_fv = 0
                # Find the lowest price at which the the auction amount is sold out. 
                price = bid[2]
                
            else:
                # Else, decrement auction amount by the bid_amount for the most recent bid
                total_offering_fv = total_offering_fv - bid[1]
            count = count + 1
            
    print(count, "bids were successful in the auction.  ")
    ytm = bond_yield_to_maturity(100, c, n, m, price)
    print(f"The auction clearing price was ${price:.3f}, i.e., YTM is {ytm:.6f} per year.")
    print("Here are the results for all bids: ")
    return (sortedBids)


if __name__ == '__main__':

    # read in the bids
    bids = collect_bids('./bond_bids.csv')
    print("Here are all the bids:")
    print_bids(bids)
    print()

    # process the bids in an auction of $500,000 of 5-year 3% semi-annual coupon bonds
    processed_bids = find_winning_bids(bids, 500000, 0.03, 5, 2)
    print_bids(processed_bids)