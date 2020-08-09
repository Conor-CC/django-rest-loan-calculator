from django.contrib import admin
from cflow.loanCalc.models import MonthlyRepaymentCalc, RepaymentCountCalc


@admin.register(MonthlyRepaymentCalc)
class MonthlyRepaymentCalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_amount', 'no_repayments',
                    'monthly_repayment_amount', 'created')


@admin.register(RepaymentCountCalc)
class RepaymentCountCalcAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_amount', 'monthly_repayment_amount',
                    'no_repayments', 'created')
