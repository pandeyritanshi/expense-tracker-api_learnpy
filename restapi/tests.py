from django.test import TestCase
from restapi import models

# Create your tests here.
class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=250,
            merchant="amazon",
            description="boat headphones",
            category="electronics",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(250, inserted_expense.amount)
        self.assertEqual("amazon", inserted_expense.merchant)
        self.assertEqual("boat headphones", inserted_expense.description)
        self.assertEqual("electronics", inserted_expense.category)
