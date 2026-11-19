import argparse
from dataclasses import dataclass


@dataclass
class InvestmentAnalysis:
    property_price: float
    down_payment: float
    loan_amount: float
    monthly_mortgage: float
    annual_gross_rent: float
    annual_net_rent: float
    gross_yield_pct: float
    net_yield_pct: float
    monthly_cashflow: float
    cash_on_cash_pct: float


def calculate_monthly_mortgage(loan_amount: float, annual_rate_pct: float, years: int) -> float:
    """Calculate standard monthly annuity payment."""
    if loan_amount <= 0 or years <= 0:
        return 0.0
    if annual_rate_pct <= 0:
        return loan_amount / (years * 12)
    monthly_rate = (annual_rate_pct / 100) / 12
    months = years * 12
    return loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)


def analyze_property(
    property_price: float,
    monthly_rent: float,
    monthly_expenses: float = 0.0,
    down_payment_pct: float = 20.0,
    interest_rate_pct: float = 4.9,
    loan_years: int = 30,
    vacancy_rate_pct: float = 5.0,
) -> InvestmentAnalysis:
    """Evaluate key investment metrics for a Czech residential property."""
    down_payment = property_price * (down_payment_pct / 100)
    loan_amount = max(0.0, property_price - down_payment)
    monthly_mortgage = calculate_monthly_mortgage(loan_amount, interest_rate_pct, loan_years)

    annual_gross_rent = monthly_rent * 12
    effective_annual_rent = annual_gross_rent * (1 - vacancy_rate_pct / 100)
    annual_net_rent = effective_annual_rent - (monthly_expenses * 12)

    gross_yield_pct = (annual_gross_rent / property_price) * 100 if property_price > 0 else 0.0
    net_yield_pct = (annual_net_rent / property_price) * 100 if property_price > 0 else 0.0

    monthly_cashflow = (annual_net_rent / 12) - monthly_mortgage
    annual_cashflow = monthly_cashflow * 12
    cash_on_cash_pct = (annual_cashflow / down_payment) * 100 if down_payment > 0 else 0.0

    return InvestmentAnalysis(
        property_price=round(property_price, 2),
        down_payment=round(down_payment, 2),
        loan_amount=round(loan_amount, 2),
        monthly_mortgage=round(monthly_mortgage, 2),
        annual_gross_rent=round(annual_gross_rent, 2),
        annual_net_rent=round(annual_net_rent, 2),
        gross_yield_pct=round(gross_yield_pct, 2),
        net_yield_pct=round(net_yield_pct, 2),
        monthly_cashflow=round(monthly_cashflow, 2),
        cash_on_cash_pct=round(cash_on_cash_pct, 2),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Czech Real Estate Investment & Mortgage Calculator")
    parser.add_argument("--price", type=float, required=True, help="Purchase price in CZK")
    parser.add_argument("--rent", type=float, required=True, help="Expected monthly rent in CZK")
    parser.add_argument("--expenses", type=float, default=3500.0, help="Monthly non-recoverable costs in CZK")
    parser.add_argument("--down-payment", type=float, default=20.0, help="Down payment percentage (default: 20)")
    parser.add_argument("--rate", type=float, default=4.9, help="Annual mortgage interest rate %% (default: 4.9)")
    parser.add_argument("--years", type=int, default=30, help="Mortgage term in years (default: 30)")
    args = parser.parse_args()

    result = analyze_property(
        property_price=args.price,
        monthly_rent=args.rent,
        monthly_expenses=args.expenses,
        down_payment_pct=args.down_payment,
        interest_rate_pct=args.rate,
        loan_years=args.years,
    )

    print(f"Property Price:    {result.property_price:,.0f} CZK")
    print(f"Down Payment:      {result.down_payment:,.0f} CZK ({args.down_payment:.0f}%)")
    print(f"Loan Amount:       {result.loan_amount:,.0f} CZK")
    print(f"Monthly Mortgage:  {result.monthly_mortgage:,.0f} CZK")
    print(f"Gross Yield:       {result.gross_yield_pct:.2f} %")
    print(f"Net Yield:         {result.net_yield_pct:.2f} %")
    print(f"Monthly Cashflow:  {result.monthly_cashflow:,.0f} CZK")
    print(f"Cash-on-Cash ROI:  {result.cash_on_cash_pct:.2f} %")


if __name__ == "__main__":
    main()
