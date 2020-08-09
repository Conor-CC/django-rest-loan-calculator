from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MonthlyRepaymentCalc(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                      blank=False,
                                      validators=[MinValueValidator(1000),
                                                  MaxValueValidator(100000)])
    no_repayments = models.PositiveIntegerField(
                    validators=[MinValueValidator(1),
                                MaxValueValidator(1000)],
                                blank=False)
    monthly_repayment_amount = models.DecimalField(max_digits=6,
                                                   decimal_places=2,
                                                   blank=True)

    class Meta:
        ordering = ['created', 'loan_amount', 'no_repayments',
                    'monthly_repayment_amount']


class RepaymentCountCalc(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                      blank=False,
                                      validators=[MinValueValidator(1000),
                                                  MaxValueValidator(100000)])
    monthly_repayment_amount = models.DecimalField(max_digits=6,
                                                   decimal_places=2,
                                                   blank=False)
    no_repayments = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ['created', 'loan_amount', 'monthly_repayment_amount',
                    'no_repayments']
