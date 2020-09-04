from django.db import models

class Currency(models.Model):
    from_code = models.CharField(max_length=80)
    from_name = models.CharField(max_length=80)
    to_code = models.CharField(max_length=80)
    to_name = models.CharField(max_length=80)
    exchange_rate = models.CharField(max_length=80)
    # last_refreshed = models.DateField()
    bid = models.CharField(max_length=80)
    ask = models.CharField(max_length=80)
