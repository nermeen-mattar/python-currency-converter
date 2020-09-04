from celery.task import periodic_task
from datetime import timedelta
from convertor.models import Currency
from convertor.common import get_currency_exchange

@periodic_task(run_every=timedelta(seconds=10))
def debug_task():
    print('Ping! Pong---!')
    details = get_currency_exchange()
    currency = Currency(from_code = details["from_code"], to_code= details["to_code"], from_name = details["from_name"], to_name= details["to_name"], 
    exchange_rate = details["exchange_rate"], bid= details["bid"], ask= details["ask"])
    currency.save()