from django.contrib import admin


# Register your models here.
from .models import Category, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin"""
    list_display = ("name",)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    """Expense admin"""
    list_display = ("title", "amount", "timestamp", "category")
    list_filter = ("timestamp", "category")
    search_fields = ("title", "description")
