from django.contrib import admin
from django.urls import path, include
from cflow.loanCalc import urls as calc_urls
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='loan-calc')),
    path('admin/', admin.site.urls, name='admin-app'),
    path('loan-calc/', include(calc_urls), name='loan-calc'),
]
