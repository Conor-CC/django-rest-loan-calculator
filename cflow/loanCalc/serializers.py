from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cflow.loanCalc.models import MonthlyRepaymentCalc, RepaymentCountCalc
from django.core.validators import MaxValueValidator, MinValueValidator

# Calculation Serializers


class CalcMonthlyRepaymentSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=6, decimal_places=2,
                                           validators=[MinValueValidator(750),
                                                       MaxValueValidator(100000)
                                                       ])
    no_repayments = serializers.IntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(1000)
                                                         ])

    class Meta:
        model = MonthlyRepaymentCalc
        fields = ['loan_amount', 'no_repayments',
                  'monthly_repayment_amount']


class CalcRepaymentCountSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=6, decimal_places=2,
                                           validators=[MinValueValidator(750),
                                                       MaxValueValidator(100000)
                                                       ])
    monthly_repayment_amount = serializers.DecimalField(max_digits=6,
                                                        decimal_places=2)

    class Meta:
        model = RepaymentCountCalc
        fields = ['loan_amount', 'monthly_repayment_amount',
                  'no_repayments']


# List Serializers

class MonthlyRepaymentsSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=6, decimal_places=2)
    no_repayments = serializers.IntegerField()
    monthly_repayment_amount = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = MonthlyRepaymentCalc
        fields = ['id', 'created', 'loan_amount', 'no_repayments',
                  'monthly_repayment_amount']


class RepaymentCountsSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=6, decimal_places=2)
    monthly_repayment_amount = serializers.DecimalField(max_digits=6, decimal_places=2)
    no_repayments = serializers.IntegerField()

    class Meta:
        model = RepaymentCountCalc
        fields = ['id', 'created', 'loan_amount', 'monthly_repayment_amount',
                  'no_repayments']
