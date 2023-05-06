# imports for django rest framework tests
from rest_framework.test import APITestCase, APIClient
from .models import Expense


class ExpensesTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        # create 3 expenses
        Expense.objects.bulk_create([
            Expense(title="Expense 1", amount=100, description="Expense 1 description"),
            Expense(title="Expense 2", amount=200, description="Expense 2 description"),
            Expense(title="Expense 3", amount=300, description="Expense 3 description"),
        ])
    
    def test_expenses_list(self):
        response = self.client.get("/api/expenses/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
    
    def test_expense_detail(self):
        response = self.client.get("/api/expenses/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Expense 1")
        self.assertEqual(response.data["amount"], "100.00")
        self.assertEqual(response.data["description"], "Expense 1 description")

    def test_expense_create(self):
        response = self.client.post("/api/expenses/", {
            "title": "Expense 4",
            "amount": 400,
            "description": "Expense 4 description",
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["title"], "Expense 4")
        self.assertEqual(response.data["amount"], "400.00")
        self.assertEqual(response.data["description"], "Expense 4 description")
    
    def test_expense_delete(self):
        response = self.client.delete("/api/expenses/1/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Expense.objects.count(), 2)

    def tearDown(self) -> None:
        Expense.objects.all().delete()
