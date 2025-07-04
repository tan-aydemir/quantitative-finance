---

# Black-Scholes-Merton Option Pricing Framework

**Author:** Tan Aydemir
**Email:** [taydemir@bu.edu](mailto:taydemir@bu.edu)

## Overview

This repository provides an object-oriented implementation of the Black-Scholes-Merton (BSM) model for pricing European call and put options. It includes tools for computing option values, deltas, and implied volatilities. The framework supports detailed parameter configuration and can generate sensitivity tables based on the underlying asset price.

---

## File Descriptions

### `bsm_option.py`

Implements the core classes for pricing European options using the Black-Scholes-Merton model.

**Base class: `BSMOption`**

* Encapsulates option parameters such as stock price (`s`), strike price (`x`), time to maturity (`t`), volatility (`sigma`), risk-free rate (`rf`), and dividend yield (`div`)
* Computes intermediary variables `d1`, `d2`, and their cumulative normal values
* Provides the structure for `.value()` and `.delta()` methods, which are defined in subclasses

**Subclasses:**

* `BSMEuroCallOption`: Prices a European call option
* `BSMEuroPutOption`: Prices a European put option

Each subclass implements:

* `.value()` – Computes the option price
* `.delta()` – Computes the option delta (rate of change with respect to underlying)

---

### `bsm_analysis.py`

Provides utility functions for analyzing option sensitivity and calculating implied volatility.

**Functions:**

* `generate_option_value_table(s, x, t, sigma, rf, div)`
  Generates a table showing how call and put prices (and their deltas) change with the underlying asset price.

* `calculate_implied_volatility(option, market_value)`
  Estimates the implied volatility using a bisection search to match a given market price.

---

## Example Usage

```python
from bsm_option import BSMEuroCallOption
from bsm_analysis import calculate_implied_volatility

# Instantiate a European call option
call = BSMEuroCallOption(
    s=100,     # current stock price
    x=100,     # strike price
    t=0.5,     # time to maturity in years
    sigma=0.25,
    rf=0.04,
    div=0.02
)

# Compute option value and delta
print("Call Option Value:", call.value())
print("Call Delta:", call.delta())

# Compute implied volatility from observed market price
implied_vol = calculate_implied_volatility(call, value=10.5)
print("Implied Volatility:", implied_vol)
```

---

## Output Sample

```
Change in option values w.r.t. change in stock price:
      price      call value  put value   call delta  put delta
$      80.00        0.1814      14.6135      0.0071      0.9049
$      81.00        0.2882      14.1972      0.0098      0.8948
...
$     100.00        5.2162       4.2571      0.4605     -0.4822
...
```

---

## Dependencies

* `math`
* `scipy` (for normal distribution functions)

Install required packages with:

```bash
pip install scipy
```
---
