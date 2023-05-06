from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """
    Description: Serializer for Expense model
    Model: Expense
    Fields: title, amount, timestamp, description, category
    """
    class Meta:
        model = Expense
        fields = ("title", "amount", "timestamp", "description", "category")
