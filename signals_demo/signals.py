import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def demo_signal_handler(sender, instance, created, **kwargs):
    """
    A single signal handler that executes different logic based on the 
    instance name to prove Django's default signal behaviors.
    """
    
    # Q1: Prove Synchronous Execution
    if instance.name == "sync_test":
        time.sleep(2)
        
    # Q2: Prove Same Thread Execution
    elif instance.name == "thread_test":
        # Attach the thread ID to the instance so the test can read it
        instance.signal_thread_id = threading.get_ident()
        
    # Q3: Prove Same Database Transaction
    elif instance.name == "transaction_test":
        # Raise an error to trigger a database rollback
        raise Exception("Intentional Exception to force rollback")