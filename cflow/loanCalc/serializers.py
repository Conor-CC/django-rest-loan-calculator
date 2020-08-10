from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cflow.loanCalc.models import MonthlyRepaymentCalc, RepaymentCountCalc, InterestRateCalc
from django.core.validators import MaxValueValidator, MinValueValidator

# Calculation Serializers


class CalcMonthlyRepaymentSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=10, decimal_places=2,
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
    loan_amount = serializers.DecimalField(max_digits=10, decimal_places=2,
                                           validators=[MinValueValidator(750),
                                                       MaxValueValidator(100000)
                                                       ])
    monthly_repayment_amount = serializers.DecimalField(max_digits=10,
                                                        decimal_places=2)

    class Meta:
        model = RepaymentCountCalc
        fields = ['loan_amount', 'monthly_repayment_amount',
                  'no_repayments']


class CalcInterestRateSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=10, decimal_places=2,
                                           validators=[MinValueValidator(750),
                                                       MaxValueValidator(100000)
                                                       ])
    monthly_repayment_amount = serializers.DecimalField(max_digits=10,
                                                        decimal_places=2)
    no_repayments = serializers.IntegerField(validators=[MinValueValidator(1),
                                                         MaxValueValidator(1000)
                                                         ])
    threshold_used = serializers.FloatField(validators=[MinValueValidator(0),
                                                        MaxValueValidator(1)])

    class Meta:
        model = InterestRateCalc
        fields = ['loan_amount', 'monthly_repayment_amount',
                  'no_repayments', 'interest_rate_annual', 'threshold_used',
                  'above_threshold']


# List Serializers

class MonthlyRepaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthlyRepaymentCalc
        fields = ['id', 'created', 'loan_amount', 'no_repayments',
                  'monthly_repayment_amount']


class RepaymentCountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepaymentCountCalc
        fields = ['id', 'created', 'loan_amount', 'monthly_repayment_amount',
                  'no_repayments']


class InterestRatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterestRateCalc
        fields = ['id', 'created', 'loan_amount', 'monthly_repayment_amount',
                  'no_repayments', 'interest_rate_annual', 'threshold_used',
                  'above_threshold']
