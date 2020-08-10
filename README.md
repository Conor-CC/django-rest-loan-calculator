# Django REST Loan Calculator Application for Capital Flow

Django REST Loan Calculator Application is used for the resolution and storage
of the following calculations/operations pertaining to loans:

- **Monthly Repayment Calculator**, based on the Principal (loan_amount) and number
  of repayment Periods (no_repayments). Based on the Annuity Formula.
- **Repayment Count Calculator**, based on the Principal (loan_amount) and Monthly
  Repayment Ammount (monthly_repayment_amount). Also based on the Annuity
  Formula.
- **Interest Rate Calculator**, returns the Interest Rate of a loan and determines
  whether or not the figure is above a certain specified interest rate threshold.

All of these functions are implemented in `cflow/loanCalc/calculators.py` and
can have their parameters tweaked by modifying `cflow/loanCalc/config.py`. This
configuration file also allows for the specification of whether or not the result
of a certain calculation should be saved to the database or not with the 'save_results'
configuration option as seen below.

```python
# cflow/loanCalc/config.py
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
```
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
