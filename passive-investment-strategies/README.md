# Passive Investment Strategies: Dollar-Cost Averaging & Portfolio Rebalancing

**Author:** Tan Aydemir
**Email:** [taydemir@bu.edu](mailto:taydemir@bu.edu)

## Overview

This project models and evaluates two passive investment strategies—**Dollar-Cost Averaging (DCA)** and **Target-Weight Portfolio Rebalancing**—across a portfolio of stocks. It examines how disciplined, unemotional investing methods perform under varying market conditions, using historical stock price data.

It also compares multiple portfolio structures (equal-weighted and mean-variance efficient) with and without periodic rebalancing, and evaluates portfolio risk using **10-day Value at Risk (VaR)** and **Maximum Drawdown**.

---

## Strategies Implemented

### 1. **Dollar-Cost Averaging**

Invests a fixed amount of money at regular intervals regardless of asset price. This strategy is applied to both single stocks and portfolios.

* Function: `dollar_cost_average(prices, total_inv=10000, num_purchases=12)`
* Result: A time series of portfolio values created by consistently investing in the same asset over time.

### 2. **Target-Weight Portfolio**

Constructs a portfolio with fixed weights assigned to each asset and tracks its value over time.

* Function: `create_target_weight_portfolio(prices, target_weights, initial_value=10000)`

### 3. **Rebalancing Strategy**

Periodically adjusts the portfolio back to its original weights, ensuring alignment with target allocations.

* Function: `create_rebalanced_portfolio(prices, target_weights, rebalance_freq, initial_value=10000)`

---

## Performance Analysis Tools

### - **Relative Weight Over Time**

Visualizes how asset weights evolve with or without rebalancing.
Function: `plot_relative_weights_over_time(values)`

### - **Return Comparison**

Plots and compares cumulative market returns vs. strategy returns.
Function: `compare_returns(df)`

---

## Risk Metrics

* **10-Day Value at Risk (VaR)**:
  Estimates potential loss with 98% confidence over 10 trading days.
  Function: `calculate_10_day_var(prices, weight, initial_value)`

* **Maximum Drawdown**:
  Measures the peak-to-trough decline in portfolio value.
  Function: `compute_drawdown(prices, weight, rebalance_freq, initial_value)`

---

## Example Usage

```python
from a13task1 import *

# Load historical price data
df = pd.read_csv('NKE.csv')
df.index = pd.to_datetime(df['Date'])
df = df.loc['2017-01-01':'2018-01-01']
df.rename(columns={'Adj Close': 'NKE'}, inplace=True)

# Apply Dollar-Cost Averaging
portfolio_df = dollar_cost_average(df['NKE'], total_inv=10000, num_purchases=12)

# Compare market vs strategy returns
portfolio_df['market'] = df['NKE']
returns = compare_returns(portfolio_df)

# Plot asset weights over time in a 50/50 NKE-AAPL portfolio
combined_df = create_target_weight_portfolio(df, {'NKE': 0.5, 'AAPL': 0.5})
plot_relative_weights_over_time(combined_df)
```

---

## Dependencies

* `pandas`
* `numpy`
* `matplotlib`

Install them via:

```bash
pip install pandas numpy matplotlib
```

---

