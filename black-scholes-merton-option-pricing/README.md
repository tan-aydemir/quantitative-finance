---

# Black-Scholes-Merton Option Pricing Framework

**Author:** Tan Aydemir
**Email:** [taydemir@bu.edu](mailto:taydemir@bu.edu)

## Overview

This repository provides a modular implementation of the Black-Scholes-Merton (BSM) model for pricing European options. It supports pricing of vanilla call and put options, computing option deltas, generating sensitivity tables, and estimating implied volatility via numerical methods.

---

## Contents

### `bsm_option.py`

Defines the core BSM model classes.

* `BSMOption`: Base class that encapsulates shared attributes and methods (e.g., `d1`, `d2`, and their cumulative probabilities).
* `BSMEuroCallOption`: Prices European call options.
* `BSMEuroPutOption`: Prices European put options.

Each subclass includes:

* `.value()`: Computes the theoretical option price.
* `.delta()`: Computes the option’s sensitivity to changes in the underlying asset.

---

### `bsm_analysis.py`

Provides utilities for option analysis and diagnostics.

* `generate_option_value_table(...)`: Creates a table of option prices and deltas as the underlying price changes.
* `calculate_implied_volatility(...)`: Estimates implied volatility using bisection search to match a given market price.

---

## Example Usage

```python
from bsm_option import BSMEuroCallOption
from bsm_analysis import calculate_implied_volatility

# Create a call option
call = BSMEuroCallOption(s=100, x=95, t=0.5, sigma=0.2, rf=0.05, div=0.01)

# Price and delta
print(call.value())
print(call.delta())

# Implied volatility given market price
iv = calculate_implied_volatility(call, value=8.5)
print("Implied Volatility:", iv)
```

---

## Dependencies

* `math`
* `scipy.stats.norm`

Install with:

```bash
pip install scipy
```

---

