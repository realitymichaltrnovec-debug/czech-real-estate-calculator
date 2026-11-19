# Czech Real Estate Calculator

Open-source Python library and command-line tool for evaluating residential real estate investments, rental yields, mortgage payments, and cash-on-cash return tailored to the Czech property market.

## Features
- **Gross & Net Rental Yield** calculation including vacancy rate and operating expenses
- **Annuity Mortgage Calculator** with configurable LTV / down payment, interest rate, and maturity
- **Monthly Cashflow & Cash-on-Cash ROI** modeling
- Zero external dependencies (pure Python 3.10+ standard library)

## Quick Start

```bash
python3 calculator.py --price 6500000 --rent 24000 --expenses 3500 --down-payment 20 --rate 4.9 --years 30
