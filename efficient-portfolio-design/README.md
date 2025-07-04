
# Portfolio Optimization and Efficient Frontier Analysis

**Author:** Tan Aydemir
**Email:** [taydemir@bu.edu](mailto:taydemir@bu.edu)

## Overview

This project implements a suite of tools for analyzing portfolio performance using historical stock data. It includes functionality for computing portfolio returns, standard deviation, global minimum variance portfolios, and constructing efficient frontiers. The toolkit also provides visualization methods for price trends, cumulative returns, and risk-return tradeoffs.

---

## Contents

### `portfolio_math.py`

Provides core quantitative functions for portfolio construction and optimization.

**Key functions:**

* `calc_portfolio_return(e, w)`: Computes expected return for a portfolio with weights `w`.
* `calc_portfolio_stdev(v, w)`: Computes standard deviation of a portfolio.
* `calc_global_min_variance_portfolio(v)`: Returns weights for the global minimum variance portfolio.
* `calc_min_variance_portfolio(e, v, r)`: Returns weights for a target-return minimum variance portfolio.
* `calc_efficient_portfolios_stdev(e, v, rs)`: Returns standard deviations of efficient portfolios across a range of target returns.
* `get_stock_prices_from_csv_files(symbols)`: Loads adjusted closing prices for specified tickers.
* `get_stock_returns_from_csv_files(symbols)`: Computes daily percentage returns.
* `get_covariance_matrix(returns)`: Returns the covariance matrix of asset returns.

---

### `bond_math.py`

Includes basic bond pricing and analysis tools.

**Key functions:**

* `bond_price(times, cashflows, rate)`: Calculates present value of bond cash flows.
* `bootstrap(cashflows, prices)`: Extracts implied discount factors from bond prices.
* `bond_duration(times, cashflows, rate)`: Computes Macaulay duration of a bond.

---

### `portfolio_plotting.py`

Visualizes stock performance and portfolio efficiency using Matplotlib.

**Key visualizations:**

* `plot_stock_prices(symbols)`: Plots historical adjusted closing prices.
* `plot_stock_cumulative_change(symbols)`: Visualizes cumulative returns for multiple assets.
* `plot_efficient_frontier(symbols)`: Plots the efficient frontier of achievable portfolios based on historical data.

---

## Example Usage

```python
from portfolio_plotting import plot_efficient_frontier

symbols = ['AAPL', 'GOOG', 'DIS', 'KO', 'WMT']
plot_efficient_frontier(symbols)
```

---

## Dependencies

* `numpy`
* `pandas`
* `matplotlib`

Install dependencies via:

```bash
pip install numpy pandas matplotlib
```

---

