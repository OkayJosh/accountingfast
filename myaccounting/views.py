from rest_framework import viewsets

from .serializers import IncomeSerializer, ExpenseSerializer, OtherFinancialsSerializer, AccountInfoSerializer

from .models import Income, Expense, OtherFinancials, AccountInfo

class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

class OtherFinancialsViewSet(viewsets.ModelViewSet):
    serializer_class = OtherFinancialsSerializer
    queryset = OtherFinancials.objects.all()

class AccountInfoViewSet(viewsets.ModelViewSet):
    serializer_class = AccountInfoSerializer
    queryset = AccountInfo.objects.all()