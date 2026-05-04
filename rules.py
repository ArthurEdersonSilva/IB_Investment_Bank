# Final Mapping: Sub-areas, Parent Departments, and Product Access
ACCESS_RULES = {
    # 1. Investment Banking (IB)
    "M&A": {
        "parent": "Investment Banking",
        "products": ["Valuation", "Deal Structure"]
    },
    "ECM": {
        "parent": "Investment Banking",
        "products": ["Stocks", "IPO", "Follow-on", "Hybrid Structures"]
    },
    "DCM": {
        "parent": "Investment Banking",
        "products": ["Debentures", "Bonds", "Convertibles"]
    },
    # 2. Sales & Trading
    "Sales": {
        "parent": "Sales & Trading",
        "products": ["Stocks", "Fixed Income", "Derivatives", "FX"]
    },
    "Trading": {
        "parent": "Sales & Trading",
        "products": ["Stocks", "Fixed Income", "Derivatives", "Options", "Futures", "Swaps", "FX"]
    },
    "Structuring": {
        "parent": "Sales & Trading",
        "products": ["COE"]
    },
    # 3. Research
    "Equity Research": {
        "parent": "Research",
        "products": ["Stocks", "Buy/Sell Recommendations"]
    },
    "Macro Research": {
        "parent": "Research",
        "products": ["Economic Analysis", "Sector Analysis"]
    },
    "Credit": {
        "parent": "Research",
        "products": ["Debentures", "Bonds"]
    },
    # 4. Asset Management
    "Fund Management": {
        "parent": "Asset Management",
        "products": ["Stocks", "Fixed Income", "Derivatives", "FX", "Funds"]
    },
    "Quantitative Management": {
        "parent": "Asset Management",
        "products": ["Stocks", "Fixed Income", "Derivatives", "FX", "Funds"]
    },
    # 5. Wealth Management
    "Advisory": {
        "parent": "Wealth Management",
        "products": ["Funds", "Stocks", "Fixed Income", "COE", "Pension"]
    },
    "Portfolio Management": {
        "parent": "Wealth Management",
        "products": ["Funds", "Stocks", "Fixed Income", "COE", "Pension"]
    },
    "Financial Planning": {
        "parent": "Wealth Management",
        "products": ["Funds", "Stocks", "Fixed Income", "COE", "Pension"]
    },
    # 6. Private Equity / Venture Capital
    "Origination": {
        "parent": "Private Equity",
        "products": ["Private Equity", "Structured Debt"]
    },
    "Investment Team": {
        "parent": "Private Equity",
        "products": ["Private Equity", "Structured Debt"]
    },
    "Portfolio Management (PE)": {
        "parent": "Private Equity",
        "products": ["Private Equity", "Structured Debt"]
    },
    # 7. Risk (Risk Management)
    "Market Risk": {
        "parent": "Risk Management",
        "products": ["Stocks", "Derivatives", "Fixed Income", "FX"]
    },
    "Credit Risk": {
        "parent": "Risk Management",
        "products": ["Stocks", "Derivatives", "Fixed Income", "FX"]
    },
    "Liquidity Risk": {
        "parent": "Risk Management",
        "products": ["Stocks", "Derivatives", "Fixed Income", "FX"]
    },
    "Operational Risk": {
        "parent": "Risk Management",
        "products": ["Stocks", "Derivatives", "Fixed Income", "FX"]
    }
}