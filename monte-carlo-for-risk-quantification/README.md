
# Monte Carlo Simulation for Risk Quantification

**Author:** Tan Aydemir
**Email:** [taydemir@bu.edu](mailto:taydemir@bu.edu)

## Overview

This project implements tools to simulate stock price paths and quantify key financial risk measures. It includes a Monte Carlo simulation engine based on geometric Brownian motion and supports the computation of Value at Risk (VaR) and drawdown statistics, both from historical data and simulated future scenarios.

These tools provide a foundation for evaluating the risk of individual assets or portfolios under both model-based and non-parametric approaches.

---

## Contents

### `mc_stock_simulator.py`

Simulates asset price evolution using Monte Carlo methods.

**Class: `MCStockSimulator`**

* `generate_simulated_stock_returns()`: Simulates log returns.
* `generate_simulated_stock_values()`: Produces a simulated price path.
* `plot_simulated_stock_values(num_trials=1)`: Visualizes one or more simulated price paths.

---

### `var_calculations.py`

Computes **Value at Risk (VaR)** using both model-based and historical approaches.

**Functions:**

* `compute_model_var_pct(mu, sigma, x, n)`: Computes the n-day model-based VaR as a percent using a normal distribution.
* `compute_historical_var_pct(returns, x, n)`: Computes historical VaR using past return quantiles.

---

### `drawdown_analysis.py`

Calculates and visualizes **drawdowns**, which represent the peak-to-trough decline in asset value.

**Functions:**

* `compute_drawdown(prices)`: Calculates dollar and percentage drawdowns based on rolling maximums.
* `plot_drawdown(df)`: Visualizes price vs. peak price, and drawdown percentage over time.
* `run_mc_drawdown_trials(...)`: Runs Monte Carlo simulations to estimate maximum drawdown distributions over a specified horizon.

---

## Example Usage

**Model-based VaR:**

```python
var_pct = compute_model_var_pct(mu=0.001, sigma=0.02, x=0.99, n=5)
print(f"5-day 99% VaR: {var_pct:.4f}")
```

**Monte Carlo drawdown simulation:**

```python
series = run_mc_drawdown_trials(
    init_price=100,
    years=10,
    r=0.08,
    sigma=0.25,
    trial_size=252,
    num_trials=1000
)
print(series.describe())
```

---

## Dependencies

* `numpy`
* `pandas`
* `matplotlib`
* `scipy`

Install dependencies with:

```bash
pip install numpy pandas matplotlib scipy
```

---

