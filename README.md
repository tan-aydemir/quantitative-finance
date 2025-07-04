# Quantitative Finance Projects

**Author:** Tan Aydemir  
**Email:** taydemir@bu.edu

This repository is a curated collection of quantitative finance projects focused on modeling risk, pricing derivatives, evaluating trading strategies, and analyzing portfolio performance. Each project applies key concepts from financial engineering and computational finance through practical implementation in Python.

---

## Overview

These projects explore a wide range of topics, including:

- Derivative Pricing: Black-Scholes and Binomial Trees for European and Exotic Options  
- Risk Quantification: Monte Carlo simulation, Value at Risk (VaR), and Drawdown  
- Investment Strategies: Passive strategies like dollar-cost averaging and rebalancing  
- Signal-Driven Trading: Rule-based trading using interest rate shifts and technical indicators  
- Portfolio Theory: Efficient frontier construction, mean-variance optimization, and backtesting

The goal is to bridge theory with practical modeling — offering functional tools for real-world financial analysis.

---

## Project Breakdown

### 1. Black-Scholes Option Pricing  
Implements the Black-Scholes-Merton framework for pricing European call and put options.  
Includes delta calculations, implied volatility estimation, and sensitivity analysis.

Files: `bsm_option.py`, `bsm_analysis.py`

---

### 2. Binomial Tree for Exotic Options  
Prices European-style exotic derivatives like Asian and Lookback options.  
Simulates asset price paths using geometric Brownian motion.

Files: `european_mc_stock.py`, `european_mc_exotic_options.py`

---

### 3. Risk Quantification Tools  
Simulates stock price paths and computes historical/model-based Value at Risk (VaR).  
Includes Monte Carlo simulations to estimate drawdown distributions.

Files: `mc_stock_simulator.py`, `value_at_risk.py`, `drawdown_analysis.py`

---

### 4. Signal-Based Strategy Using Interest Rates  
Implements a trading strategy based on changes in long-term interest rates.  
Measures and visualizes market, strategy, and abnormal returns.

File: `interest_rate_strategy.py`

---

### 5. Technical Strategy Backtesting  
Backtests a Bollinger Band–based long/short strategy on historical price data.  
Compares market and strategy performance with cumulative return plots.

File: `bollinger_backtest.py`

---

### 6. Portfolio Strategy and Risk Framework  
Simulates passive investment strategies like dollar-cost averaging and rebalancing.  
Builds and tracks multi-asset portfolios with custom weight allocations.

File: `portfolio_strategy_builder.py`

---

### 7. Portfolio Comparison and Risk Evaluation  
Constructs and evaluates four portfolio strategies:  
- Equal weights with and without rebalancing  
- Mean-variance optimized with and without rebalancing  

Assesses performance using 10-day VaR and maximum drawdown.

File: `portfolio_risk_analysis.py`

---

## Output & Visuals

Some projects include accompanying visuals that summarize results. These are stored in:

- `a11graphs.pdf`
- `a12graphs.pdf`

They visualize cumulative returns, strategy comparisons, and drawdowns.

---

## Requirements

Ensure the following packages are installed:

```bash
pip install numpy pandas matplotlib scipy
