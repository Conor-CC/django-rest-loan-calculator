import math
from cflow.loanCalc.config import CalculationSettings as cs


# https://financeformulas.net/Annuity_Payment_Formula.html
# Monthly_Repayments = (Monthly_Interest * Present_Value)
#                       / (1 - [1 + Monthly_Interest]^-n)

def calcMonthlyRepayments(loan_amount, no_repayments):
    monthly_interest = (cs['monthly_repayment_calc']['annual_interest_rate']
                        / 12)
    numerator = monthly_interest * loan_amount
    denominator = 1 - (pow((1 + monthly_interest), (-1 * no_repayments)))
    result = numerator / denominator
    # additional result validation could be carried out here
    return round(result, 2)


# No_of_Repayments = ln([(1 - (Present_Value * Monthly_Interest))^-1])
#                       / ln(1 + Monthly_Interest)

def calcRepaymentCount(loan_amount, monthly_repayment_amount):
    monthly_interest = (cs['repayment_count_calc']['annual_interest_rate']
                        / 12)
    numerator = math.log(
                pow((1 - ((loan_amount * monthly_interest)
                          / monthly_repayment_amount)
                     ), -1))
    denominator = math.log(1 + monthly_interest)
    result = numerator / denominator
    return int(round(result))
