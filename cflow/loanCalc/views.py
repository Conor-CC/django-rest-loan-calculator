from cflow.loanCalc.models import MonthlyRepaymentCalc, RepaymentCountCalc
from cflow.loanCalc.serializers import MonthlyRepaymentsSerializer, RepaymentCountsSerializer
from cflow.loanCalc.serializers import CalcMonthlyRepaymentSerializer, CalcRepaymentCountSerializer
from cflow.loanCalc.config import CalculationSettings as cs
from cflow.loanCalc.calculators import calcMonthlyRepayments, calcRepaymentCount
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework import status, generics


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'monthly-repayment-list': reverse('list-monthly-repayment',
                                          request=request, format=format),
        'repayment-count-list': reverse('list-repayment-count',
                                        request=request, format=format),
    })


# Calculation Views


class CalcMonthlyRepayments(APIView):
    """
    Request a Monthly Repayment Calculation (loan_amount / no_repayments)
    """

    def post(self, request, format=None):
        serializer = CalcMonthlyRepaymentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            loan_amount = serializer.validated_data["loan_amount"]
            no_repayments = serializer.validated_data["no_repayments"]
            calc = calcMonthlyRepayments(loan_amount, no_repayments)
            req_status = status.HTTP_200_OK

            if cs['monthly_repayment_calc']['save_results']:
                serializer.save(monthly_repayment_amount=calc)
                req_status = status.HTTP_201_CREATED
            # calc must be used in the Response instead of addressing the
            # serializer.data attribute as 'monthly_repayment_amount' will not
            # always be present i.e if results are not saved to database.
            return Response({'result': "{:.2f}".format(calc)},
                            status=req_status)


class CalcRepaymentCount(APIView):
    """
    Request a Repayment Count Calculation, i.e how many repayments must be made
    on a loan (loan_amount / monthly_repayment_amount)
    """

    def post(self, request, format=None):
        serializer = CalcRepaymentCountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            loan_amount = serializer.validated_data["loan_amount"]
            monthly_repayment_amount = serializer.validated_data["monthly_repayment_amount"]
            calc = calcRepaymentCount(loan_amount, monthly_repayment_amount)
            print(calc)
            req_status = status.HTTP_200_OK

            if cs['repayment_count_calc']['save_results']:
                serializer.save(no_repayments=calc)
                req_status = status.HTTP_201_CREATED

            return Response({'result': calc},
                            status=req_status)


# List Views


class ListMonthlyRepayments(generics.ListAPIView):
    """
    List all stored 'Monthly Repayment' Calculations
    """
    queryset = MonthlyRepaymentCalc.objects.all()
    serializer_class = MonthlyRepaymentsSerializer


class ListRepaymentCounts(generics.ListAPIView):
    """
    List all stored 'Repayment Count' Calculations
    """
    queryset = RepaymentCountCalc.objects.all()
    serializer_class = RepaymentCountsSerializer


# Retrieve Views


class RetrieveMonthlyRepayment(generics.RetrieveAPIView):
    """
    Retrieve an individual stored 'Monthly Repayment' Calculation
    """
    queryset = MonthlyRepaymentCalc.objects.all()
    serializer_class = MonthlyRepaymentsSerializer


class RetrieveRepaymentCount(generics.RetrieveAPIView):
    """
    Retrieve an individual stored 'Repayment Count' Calculation
    """
    queryset = RepaymentCountCalc.objects.all()
    serializer_class = RepaymentCountsSerializer
