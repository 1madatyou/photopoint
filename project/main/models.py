from django.db import models


class CurrencyRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    create_date = models.DateTimeField(auto_now_add=True)
