from django.db import models


class Contact(models.Model):
    """Подписка по email"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
   # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
