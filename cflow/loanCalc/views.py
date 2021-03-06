from cflow.loanCalc.models import MonthlyRepaymentCalc, RepaymentCountCalc, InterestRateCalc
from cflow.loanCalc.serializers import MonthlyRepaymentsSerializer, RepaymentCountsSerializer, InterestRatesSerializer
from cflow.loanCalc.serializers import CalcMonthlyRepaymentSerializer, CalcRepaymentCountSerializer, CalcInterestRateSerializer
from cflow.loanCalc.calculators import calcMonthlyRepayments, calcRepaymentCount, isInterestAboveThreshold
from cflow.loanCalc.config import CalculationSettings as cs
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
        'interest-rate-list': reverse('list-interest-rate',
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
            calc = calcMonthlyRepayments(float(loan_amount), no_repayments)
            req_status = status.HTTP_200_OK

            if cs['monthly_repayment_calc']['save_results']:
                serializer.save(monthly_repayment_amount=calc)
                req_status = status.HTTP_201_CREATED

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
            monthly_repayment = serializer.validated_data["monthly_repayment_amount"]
            calc = calcRepaymentCount(float(loan_amount), float(monthly_repayment))
            req_status = status.HTTP_200_OK

            if cs['repayment_count_calc']['save_results']:
                serializer.save(no_repayments=calc)
                req_status = status.HTTP_201_CREATED

            return Response({'result': calc},
                            status=req_status)


class CalcInterestRate(APIView):
    """
    Calculates the interest rate of a loan based on the Loan Amount (Principal),
    the number of repayments (Periods) and the Monthly Payment Amount. This result
    is cross checked with a preconfigured minimum interest threshold.
    """

    def post(self, request, format=None):
        threshold_used = cs['interest_rate_calc']['threshold']
        request.data['threshold_used'] = threshold_used
        serializer = CalcInterestRateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            loan_amount = serializer.validated_data["loan_amount"]
            no_repayments = serializer.validated_data["no_repayments"]
            monthly_repayment = serializer.validated_data["monthly_repayment_amount"]
            calc, above_threshold = isInterestAboveThreshold(
                                                            float(loan_amount),
                                                            no_repayments,
                                                            float(monthly_repayment),
                                                            threshold_used
                                                            )
            req_status = status.HTTP_200_OK
            if cs['interest_rate_calc']['save_results']:
                serializer.save(interest_rate_annual=calc,
                                threshold_used=0.1,
                                above_threshold=above_threshold)
                req_status = status.HTTP_201_CREATED

            return Response({'above_threshold': above_threshold,
                             'interest_rate_annual': calc,
                             'threshold_used': threshold_used},
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


class ListInterestRates(generics.ListAPIView):
    """
    List all stored 'Interest Rate' Calculations
    """
    queryset = InterestRateCalc.objects.all()
    serializer_class = InterestRatesSerializer


# Retrieve Views


class RetrieveMonthlyRepayment(generics.RetrieveDestroyAPIView):
    """
    Retrieve a stored 'Monthly Repayment' Calculation
    """
    queryset = MonthlyRepaymentCalc.objects.all()
    serializer_class = MonthlyRepaymentsSerializer


class RetrieveRepaymentCount(generics.RetrieveDestroyAPIView):
    """
    Retrieve a stored 'Repayment Count' Calculation
    """
    queryset = RepaymentCountCalc.objects.all()
    serializer_class = RepaymentCountsSerializer


class RetrieveInterestRate(generics.RetrieveDestroyAPIView):
    """
    Retrieve a stored 'Interest Rate' Calculation
    """
    queryset = InterestRateCalc.objects.all()
    serializer_class = InterestRatesSerializer
