from django.contrib import admin
from cflow.loanCalc.models import MonthlyRepaymentCalc, RepaymentCountCalc, InterestRateCalc


@admin.register(MonthlyRepaymentCalc)
class MonthlyRepaymentCalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_amount', 'no_repayments',
                    'monthly_repayment_amount', 'created')


@admin.register(RepaymentCountCalc)
class RepaymentCountCalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_amount', 'monthly_repayment_amount',
                    'no_repayments', 'created')

@admin.register(InterestRateCalc)
class InterestRateCalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_amount', 'monthly_repayment_amount',
                    'no_repayments', 'interest_rate_annual',
                    'above_threshold', 'threshold_used', 'created')
