"""
Configuration file to specify parameters of the loanCalc application.
"""
CalculationSettings = {
    'monthly_repayment_calc': {
        'save_results': True,
        'annual_interest_rate': 0.07
    },
    'repayment_count_calc': {
        'save_results': True,
        'annual_interest_rate': 0.07
    },
    'interest_rate_calc': {
        'save_results': True,
        'threshold': 0.05
    }
}
