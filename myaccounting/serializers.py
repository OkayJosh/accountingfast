from rest_framework import serializers

from .models import Income, Expense, OtherFinancials

class IncomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Income
        fields = ['name', 'amount', 'comment']

class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'comment']

class OtherFinancialsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtherFinancials
        fields = ['name', 'amount', 'comment']