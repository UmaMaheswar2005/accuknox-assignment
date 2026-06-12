import time
import threading
from django.test import TestCase, TransactionTestCase
from django.db import transaction
from .models import MyModel

class DjangoSignalsTest(TestCase):
    
    def test_q1_signals_are_synchronous(self):
        """
        By default, Django signals execute synchronously. 
        The caller must wait for the signal to finish before continuing.
        """
        start_time = time.time()
        
        # The signal will sleep for 2 seconds when it sees this name
        MyModel.objects.create(name="sync_test")
        
        elapsed_time = time.time() - start_time
        
        # If signals were async, elapsed_time would be near 0.
        self.assertGreaterEqual(elapsed_time, 2.0)

    def test_q2_signals_share_caller_thread(self):
        """
        By default, Django signals run in the exact same thread as the caller.
        """
        caller_thread_id = threading.get_ident()
        
        instance = MyModel.objects.create(name="thread_test")
        
        # The signal handler attached its thread ID to the instance
        self.assertEqual(caller_thread_id, instance.signal_thread_id)


class DjangoTransactionTest(TransactionTestCase):
    
    def test_q3_signals_share_caller_transaction(self):
        """
        By default, Django signals share the caller's database transaction.
        If the signal throws an error, the caller's database operation rolls back.
        """
        try:
            with transaction.atomic():
                # The signal will intentionally raise an Exception when it sees this name
                MyModel.objects.create(name="transaction_test")
        except Exception as e:
            self.assertEqual(str(e), "Intentional Exception to force rollback")
            
        # Verify the object was NOT saved to the database due to the rollback
        exists = MyModel.objects.filter(name="transaction_test").exists()
        self.assertFalse(exists)