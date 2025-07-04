# Binomial Asset Pricing & Options Modeling

**Author:** Tan Aydemir
**Email:** taydemir@bu.edu

## Overview

This repository implements a complete binomial tree framework for modeling asset price movements and pricing European and American options. It consists of a modular design using object-oriented Python, with flexible support for adjusting key market parameters such as volatility, interest rate, dividend yield, and number of periods.

---

## Contents

### `binomial_tree.py`

Builds a **recombinant binomial tree** to simulate the evolution of an underlying asset over time.

* Accepts inputs like initial price, volatility, risk-free rate, dividend yield, time to maturity, and number of steps.
* Automatically recalculates the tree on parameter updates.
* Includes a formatted string representation for visualization.

**Key methods:**

* `set_s()`, `set_stdev()`, `set_rf()`, etc. — Reconfigure inputs dynamically
* `build_tree()` — Reconstructs the asset price tree
* `__repr__()` — Nicely formats the tree for output

---

### `binomial_options.py`

Extends the binomial tree model to support **European and American option pricing**.

**Subclasses:**

* `BinomialEuroCallOption`
* `BinomialEuroPutOption`
* `BinomialAmericanPutOption`

**Functionality:**

* Builds the option value tree using backward induction
* Supports recomputation on input changes
* Offers formatted visual output and `.value()` method for current option price

---

### `matrix_utils.py`

Utility functions for matrix creation and manipulation. These support binomial tree construction and output formatting.

**Functions include:**

* `zeros(n, m)` – Create a matrix of zeros
* `identity_matrix(n)` – Construct identity matrices
* `transpose(M)` – Compute matrix transpose
* `swap_rows()`, `mult_row_scalar()`, `add_row_into()` – Row operations
* `print_matrix()` – Formatted matrix output

---

## Example Usage

```python
from binomial_options import BinomialEuroCallOption

# Create a European call option with given parameters
euro_call = BinomialEuroCallOption(s=100, x=105, stdev=0.2, rf=0.05, div=0.02, t=1, nper=3)

# View the option tree
print(euro_call)

# Get the option price at time 0
print("Option value:", euro_call.value())
```
---
