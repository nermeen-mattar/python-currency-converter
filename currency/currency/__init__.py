from .celery import celery_app
# from currency.tasks import check
# from datetime import datetime, timedelta

__all__ = ('celery_app',)

# check.apply_async(eta=datetime.now() + timedelta(seconds=10))
# check.delay()