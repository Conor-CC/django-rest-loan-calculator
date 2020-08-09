from cflow.loanCalc.models import MonthlyRepaymentCalc
from cflow.loanCalc.serializers import MonthlyRepaymentAmtSerializer
from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MonthlyRepaymentAmt(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        loanRepaymentCalcs = MonthlyRepaymentCalc.objects.all()
        serializer = MonthlyRepaymentAmtSerializer(loanRepaymentCalcs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MonthlyRepaymentAmtSerializer(data=request.data)
        if serializer.is_valid():
            loan_amount = serializer.validated_data["loan_amount"]
            no_repayments = serializer.validated_data["no_repayments"]
            calc = loan_amount / no_repayments
            serializer.save(monthly_repayment_amount=calc)
            return Response({
                            "monthly_repayment_amount": calc
                            }, status=status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
