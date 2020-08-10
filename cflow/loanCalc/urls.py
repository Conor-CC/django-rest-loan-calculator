from django.urls import path
from cflow.loanCalc import views

# Class Based Views
urlpatterns = [
    path('', views.api_root),

    path('monthly-repayment/', views.CalcMonthlyRepayments.as_view(),
         name='calc-monthly-repayment'),
    path('monthly-repayment/<int:pk>', views.RetrieveMonthlyRepayment.as_view(),
         name='retrieve-monthly-repayment'),
    path('monthly-repayment-list/', views.ListMonthlyRepayments.as_view(),
         name='list-monthly-repayment'),

    path('repayment-count/', views.CalcRepaymentCount.as_view(),
         name='calc-repayment-count'),
    path('repayment-count/<int:pk>', views.RetrieveRepaymentCount.as_view(),
         name='retrieve-repayment-count'),
    path('repayment-count-list/', views.ListRepaymentCounts.as_view(),
         name='list-repayment-count'),

    path('interest-rate/', views.CalcInterestRate.as_view(),
         name='calc-interest-rate'),
    path('interest-rate/<int:pk>', views.RetrieveInterestRate.as_view(),
         name='retrieve-interest-rate'),
    path('interest-rate-list/', views.ListInterestRates.as_view(),
         name='list-interest-rate'),
]
