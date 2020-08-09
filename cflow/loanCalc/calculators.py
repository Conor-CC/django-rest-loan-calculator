def calcMonthlyRepayments(loan_amount, no_repayments):
    result = float(loan_amount) / float(no_repayments)
    # additional result validation could be carried out here
    return round(result, 2)

def calcRepaymentCount(loan_amount, monthly_repayment_amount):
    result = float(loan_amount) / float(monthly_repayment_amount)
    return int(round(result))
