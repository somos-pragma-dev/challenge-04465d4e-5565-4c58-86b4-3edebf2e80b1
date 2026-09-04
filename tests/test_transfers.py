from django.test import TestCase
from core.models import Account, Transfer
from transfers.serializers import TransferSerializer

class TransferTests(TestCase):
    def setUp(self):
        self.account1 = Account.objects.create(balance=100.00, status='active')
        self.account2 = Account.objects.create(balance=200.00, status='active')

    def test_create_transfer(self):
        data = {'from_account': self.account1.id, 'to_account': self.account2.id, 'amount': 50.00, 'operation_key': '12345'}
        serializer = TransferSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        transfer = serializer.save()
        self.assertEqual(transfer.amount, 50.00)
        self.assertEqual(transfer.operation_key, '12345')