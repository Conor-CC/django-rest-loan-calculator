from django.urls import path
from cflow.loanCalc import views

# Class Based Views
urlpatterns = [
    path('monthly-repayment-amt/', views.MonthlyRepaymentAmt.as_view()),
]
