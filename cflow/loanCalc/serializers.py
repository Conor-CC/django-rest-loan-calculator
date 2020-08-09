from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cflow.loanCalc.models import MonthlyRepaymentCalc


class MonthlyRepaymentAmtSerializer(serializers.ModelSerializer):
    loan_amount = serializers.DecimalField(max_digits=6, decimal_places=2)
    no_repayments = serializers.IntegerField()

    class Meta:
        model = MonthlyRepaymentCalc
        fields = ['created', 'loan_amount', 'no_repayments',
                  'monthly_repayment_amount']


class ResultSerializer(serializers.Serializer):
    result = serializers.IntegerField()


class CalcSerializer(serializers.Serializer):
    loan_amount = serializers.IntegerField()
    no_repayments = serializers.IntegerField()
    result = serializers.IntegerField()
