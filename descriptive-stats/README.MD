# Stock Return Analysis and Descriptive Statistics

This project processes historical stock price data and calculates various descriptive statistics based on periodic returns. It reads adjusted closing prices from CSV files, computes returns, and evaluates metrics such as mean, standard deviation, covariance, correlation, R-squared, beta, and alpha.

The script uses a supporting module (`a3task1.py`) that contains custom implementations of statistical functions.

## Features

- Reads adjusted close prices from CSV files
- Calculates periodic returns for each stock
- Computes pairwise statistics between a benchmark (e.g., VTSMX) and other stocks
- Outputs results in a formatted table for easy comparison

## Files

- `main.py`: Loads stock data, computes statistics, and prints the results
- `a3task1.py`: Helper module with implementations of mean, variance, covariance, correlation, and regression

## Example Use

To run the analysis:

```bash
python main.py

