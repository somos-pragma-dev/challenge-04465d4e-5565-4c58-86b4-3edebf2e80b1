from django.test import TestCase
from core.models import Account
from accounts.serializers import AccountSerializer

class AccountTests(TestCase):
    def test_create_account(self):
        data = {'balance': 100.00, 'status': 'active'}
        serializer = AccountSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        account = serializer.save()
        self.assertEqual(account.balance, 100.00)
        self.assertEqual(account.status, 'active')