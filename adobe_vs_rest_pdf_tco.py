#!/usr/bin/env python3
"""Adobe PDF Services API vs REST PDF API Cost Model."""
import argparse
import sys

def calculate_comparison(monthly_docs):
    # Adobe PDF Services API charges approx $0.05 per document transaction
    # with complex enterprise contract minimums ($1,200/yr minimum commitment)
    adobe_per_doc = 0.05
    adobe_monthly = max(100.0, monthly_docs * adobe_per_doc)
    adobe_annual = adobe_monthly * 12

    # Cloud REST PDF API (APITemplate):
    # Basic $19 (3,000 docs), Standard $69 (12,000 docs), Enterprise $139 (25,000 docs)
    if monthly_docs <= 3000:
        cloud_tier = "Basic Plan ($19/mo)"
        cloud_monthly = 19.0
    elif monthly_docs <= 12000:
        cloud_tier = "Standard Plan ($69/mo)"
        cloud_monthly = 69.0
    elif monthly_docs <= 25000:
        cloud_tier = "Enterprise Plan ($139/mo)"
        cloud_monthly = 139.0
    else:
        cloud_tier = "Custom High-Volume ($249/mo)"
        cloud_monthly = 249.0

    cloud_annual = cloud_monthly * 12
    annual_savings = adobe_annual - cloud_annual

    return {
        "monthly_docs": monthly_docs,
        "adobe_monthly": adobe_monthly,
        "adobe_annual": adobe_annual,
        "cloud_tier": cloud_tier,
        "cloud_monthly": cloud_monthly,
        "cloud_annual": cloud_annual,
        "annual_savings": annual_savings,
        "savings_pct": (annual_savings / adobe_annual) * 100 if adobe_annual > 0 else 0.0
    }

def main():
    parser = argparse.ArgumentParser(description="Adobe PDF Services API vs REST PDF API TCO Comparison")
    parser.add_argument("--docs", type=int, default=10000, help="Monthly document count (default: 10,000)")
    args = parser.parse_args()

    r = calculate_comparison(args.docs)
    print("=" * 70)
    print(" Adobe PDF Services API vs Cloud REST PDF API Cost Comparison")
    print("=" * 70)
    print(f" Monthly Document Volume      : {r['monthly_docs']:,} documents")
    print(f" Adobe PDF Services API Cost  : ${r['adobe_monthly']:.2f}/mo (${r['adobe_annual']:.2f}/year)")
    print(f" Modern Cloud REST Plan       : {r['cloud_tier']} (${r['cloud_monthly']:.2f}/mo)")
    print(f" Modern Cloud Annual Cost     : ${r['cloud_annual']:.2f}/year")
    print("-" * 70)
    print(f" Projected Annual Savings     : ${r['annual_savings']:.2f}/yr ({r['savings_pct']:.1f}% reduction)")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())
