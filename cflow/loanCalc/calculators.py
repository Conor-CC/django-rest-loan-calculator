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


# Interest_Above_Threshold if Interest_Threshold < Calculated_Annual_Interest
# Blog post here was incredibly helpful for Interest rate calculation:
# https://blog.bossylobster.com/2012/05/reverse-calculating-interest-rate

def isInterestAboveThreshold(loan_amount, no_repayments,
                             monthly_repayment_amount,
                             threshold):
    rate = calcInterestRate(loan_amount, no_repayments,
                            monthly_repayment_amount)
    return (round(rate, 7), (rate > threshold))


# Explanation of Newton Raphson Method:
# https://mathworld.wolfram.com/NewtonsMethod.html

def newtonRaphson(approximation, f, f_prime):
    def nextValue(val):
        return val - f(val) * 1.0 / f_prime(val)

    current = approximation
    while abs(f(current)) > 10 ** (-8):
        current = nextValue(current)

    return current


def calcInterestRate(loan_amount, no_repayments, monthly_repayment_amount):
    f, f_prime = genPolynomials(loan_amount, no_repayments,
                                monthly_repayment_amount)
    approximation = m(0.1)
    result = newtonRaphson(approximation, f, f_prime)
    return m_inverse(result)


def m(r):
    return 1 + r / 12.0


def m_inverse(m_value):
    return 12.0 * (m_value - 1)


def genPolynomials(loan_amount, no_repayments, monthly_repayment_amount):
    def f(m):
        return (
                (loan_amount * (m ** (no_repayments + 1)))
                - (loan_amount + monthly_repayment_amount)
                * (m ** no_repayments)
                + monthly_repayment_amount
                )

    def f_prime(m):
        return (
                loan_amount * (no_repayments + 1) * (m ** no_repayments)
                - (loan_amount + monthly_repayment_amount)
                * no_repayments
                * (m ** (no_repayments - 1))
                )

    return (f, f_prime)
