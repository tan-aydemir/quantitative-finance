Got it. Here's a professional, clean, and natural-sounding `README.md` tailored to your codebase:

---

# Bond Pricing & Auction Simulation Toolkit

**Author:** Tan Aydemir
**Email:** taydemir@bu.edu

## Overview

This repository provides a modular toolkit for pricing fixed-income securities and simulating bond auctions. It includes tools for computing cash flows, discount factors, duration and convexity metrics, and estimating price sensitivity to interest rate changes. The package also contains a script to simulate a sealed-bid auction and determine the clearing yield.

---

## File Descriptions

### `a2task1.py` — Core Bond Pricing Functions

Includes foundational functions for fixed-income analysis:

* `cashflow_times(n, m)`: Returns a list of time periods when coupon payments are made.
* `discount_factors(r, n, m)`: Calculates discount factors for a given interest rate.
* `bond_cashflows(fv, c, n, m)`: Returns the list of periodic cash flows for a bond.
* `bond_price(fv, c, n, m, r)`: Computes the bond’s present value (price).
* `bond_yield_to_maturity(fv, c, n, m, price)`: Solves for the bond’s yield to maturity using binary search.

---

### `a2task2.py` — Duration, Convexity, and Price Sensitivity

Builds on `a2task1.py` and adds tools for analyzing interest rate risk:

* `bond_duration(...)`: Calculates duration using discounted cash flows.
* `macaulay_duration(...)`: Computes Macaulay duration.
* `modified_duration(...)`: Returns the modified duration of the bond.
* `bond_convexity(...)`: Calculates convexity to capture curvature of the price-yield relationship.
* `estimate_change_in_price1(...)`: Estimates price change using modified duration.
* `estimate_change_in_price2(...)`: Incorporates both duration and convexity in the estimate.

---

### `a2task3.py` — Bond Auction Simulation

Simulates a competitive bond auction based on bidder data from a CSV file.

* `collect_bids(filename)`: Reads bid data from a file.
* `print_bids(bids)`: Displays the bids in a formatted table.
* `find_winning_bids(...)`: Sorts bids, matches them to the offering amount, and determines the clearing price and yield.

Example usage:

```bash
python3 a2task3.py
```

This will load bids from `bond_bids.csv`, run the auction, and display the outcome

---

## Example CSV Format

The auction script expects a `bond_bids.csv` file structured as:

```
bid_id,bid_amount,bid_price
1,10000,99.50
2,15000,99.60
3,5000,99.45
...
```

---

## Notes

* All monetary values are assumed to be in dollars.
* Time periods are defined based on the frequency `m` (e.g., semiannual = 2).
* No external libraries are required.

---

Let me know if you'd like this turned into a downloadable file or rendered on your GitHub repo.
