# **Django REST Loan Calculator Application for Capitalflow**

Django REST Loan Calculator Application is used for the resolution and storage
of the following calculations/operations pertaining to loans:

- **Monthly Repayment Calculator**, based on the Principal (loan_amount) and number
  of repayment Periods (no_repayments). Based on the Annuity Formula.
- **Repayment Count Calculator**, based on the Principal (loan_amount) and Monthly
  Repayment Ammount (monthly_repayment_amount). Also based on the Annuity
  Formula.
- **Interest Rate Calculator**, returns the Interest Rate of a loan and determines
  whether or not the figure is above a certain specified interest rate threshold.
  This threshold can be configured, see `cflow/loanCalc/config.py` sample below.

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
        'save_results': False,
        'threshold': 0.05
    }
}
```
# Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.
python version 3.6

```bash
git clone https://github.com/Conor-CC/django-rest-loan-calculator
cd django-rest-loan-calculator
pip install virtualenv # If not already installed
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # Enables access to Admin Panel
python manage.py runserver
```

# Usage
To start the server, use `python manage.py runserver` in the project root. This
will open the server at `localhost:8000`. Two applications are available at the
following urls...
- **localhost:8000/admin** leads to the admin panel, super user credentials required for access.
- **localhost:8000/loan-calc** leads to all loan calculation endpoints, described below:

Remember that all results can be saved to the database or discarded by specifying
configurations in `cflow/loanCalc/config.py` with the `'save_results'` attribute.

### Monthly Repayment Calculator
Three endpoints for Requesting, Listing and Retrieving Monthly Repayment Calculations are
available.
- **localhost:8000/loan-calc/monthly-repayment/** *(POST)*: Requests a monthly repayment
  calculation with the following paramaters included in the body (given as json)
  ```json
  {
	   "loan_amount": "10000.00",
	   "no_repayments": "12"
  }
  ```
- **localhost:8000/loan-calc/monthly-repayment-list/** *(GET)*: Lists (with pagination)
  all stored Monthly Repayment Calculations & Results
- **localhost:8000/loan-calc/monthly-repayment/<id>** *(GET)*: Retrieves an individual
  Monthly Repayment Calculation & Result by id (ids can be found with the **monthly-repayment-list**
  endpoint above).

### Repayment Count Calculator
Three endpoints for Requesting, Listing and Retrieving Repayment Count Calculations are
available.
- **localhost:8000/loan-calc/monthly-repayment/** *(POST)*: Requests a repayment count
  calculation with the following paramaters included in the body (given as json)
  ```json
  {
	   "loan_amount": "30000",
	   "monthly_repayment_amount": "250"
  }
  ```
- **localhost:8000/loan-calc/repayment-count-list/** *(GET)*: Lists (with pagination)
  all stored Repayment Count Calculations & Results
- **localhost:8000/loan-calc/repayment-count/<id>** *(GET)*: Retrieves an individual
  Repayment Count Calculation & Result by id (ids can be found with the **repayment-count-list**
  endpoint above).

### Interest Rate Calculator
Three endpoints for Requesting, Listing and Retrieving Monthly Repayment Calculations are
available.
- **localhost:8000/loan-calc/interest-rate/** *(POST)*: Requests a interest rate
  calculation with the following paramaters included in the body (given as json)
  ```json
  {
  	"loan_amount": "100000",
  	"no_repayments": "360",
  	"monthly_repayment_amount": "665.30"
  }
  ```
  Returns a response like so:
  ```json
  {
    "above_threshold": true,
    "interest_rate_annual": 0.0699996,
    "threshold_used": 0.05
  }
  ```
- **localhost:8000/loan-calc/interest-rate-list/** *(GET)*: Lists (with pagination)
  all stored Interest Rate Calculations & Results
- **localhost:8000/loan-calc/interest-rate/<id>** *(GET)*: Retrieves an individual
  Interest Rate Calculation & Result by id (ids can be found with the **repayment-count-list**
  endpoint above).
