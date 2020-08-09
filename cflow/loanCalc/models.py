from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class MonthlyRepaymentCalc(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loan_amount = models.DecimalField(max_digits=6, decimal_places=2,
                                      blank=False)
    no_repayments = models.PositiveIntegerField(
                    validators=[MinValueValidator(1),
                                MaxValueValidator(10000)])
    monthly_repayment_amount = models.DecimalField(max_digits=6,
                                                   decimal_places=2,
                                                   blank=True)

    class Meta:
        ordering = ['created', 'loan_amount', 'no_repayments',
                    'monthly_repayment_amount']
