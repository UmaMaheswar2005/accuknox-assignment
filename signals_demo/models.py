from django.db import models


class MyModel(models.Model):
    """Simple model used to trigger Django signals (post_save, pre_save, etc.)"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'signals_demo'
