
# Monte Carlo Framework for Exotic Option Pricing

**Author:** Tan Aydemir
**Email:** [taydemir@bu.edu](mailto:taydemir@bu.edu)

## Overview

This repository provides a simulation-based framework for pricing exotic options using Monte Carlo methods. It includes a core stock simulation engine built on geometric Brownian motion, and an extensible hierarchy of option classes capable of pricing various path-dependent options such as Asian and Lookback options.

The modular design supports customization and extension to additional exotic derivatives.

---

## File Descriptions

### `mc_stock_simulator.py`

Simulates stock price evolution under a geometric Brownian motion process.

**Class: `MCStockSimulator`**

* `generate_simulated_stock_returns()`
* `generate_simulated_stock_values()`
* `plot_simulated_stock_values(num_trials=1)`

Parameters:

* `s`: Initial stock price
* `t`: Time horizon in years
* `mu`: Expected return
* `sigma`: Volatility
* `nper_per_year`: Number of discrete periods per year

---

### `mc_option_pricing.py`

Extends the simulator to price exotic options through Monte Carlo simulation. Each subclass implements a specific option type with customized payoff structures.

**Base class: `MCStockOption`**

* Inherits from `MCStockSimulator`
* Adds `strike price`, `risk-free rate`, and `number of trials`
* Includes `.value()` and `.stderr()` methods

**Implemented Subclasses:**

| Class Name             | Option Type   | Description                                     |
| ---------------------- | ------------- | ----------------------------------------------- |
| `MCEuroCallOption`     | European Call | Standard call based on terminal stock price     |
| `MCEuroPutOption`      | European Put  | Standard put based on terminal stock price      |
| `MCAsianCallOption`    | Asian Call    | Payoff based on average price over time         |
| `MCAsianPutOption`     | Asian Put     | Payoff based on average price over time         |
| `MCLookbackCallOption` | Lookback Call | Payoff based on maximum stock price during path |
| `MCLookbackPutOption`  | Lookback Put  | Payoff based on minimum stock price during path |

Each class implements its own logic in the `.value()` method and supports standard error reporting.

---

## Example Usage

```python
from mc_option_pricing import MCAsianCallOption

# Instantiate an Asian call option
option = MCAsianCallOption(
    s=100,
    x=95,
    t=1,
    r=0.05,
    sigma=0.25,
    nper_per_year=252,
    num_trials=10000
)

# Compute option price and standard error
print("Option Price:", option.value())
print("Standard Error:", option.stderr())
```

---

