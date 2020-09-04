from django.contrib.auth.forms import UserCreationForm
from django.forms import model_to_dict
from django.views.generic.edit import CreateView
from django.http import Http404, HttpResponseForbidden, JsonResponse
from rest_framework.decorators import api_view
from .common import get_currency_exchange
from .models import Currency
import json
#URL /
# @define_usage(returns={'url_usage': 'Dict'})
@api_view(['GET', 'POST'])
# @permission_classes((AllowAny,))
def get_exchange(request):
    if request.method == 'POST':
        details = get_currency_exchange()

        currency = Currency(from_code = details["from_code"], to_code= details["to_code"], from_name = details["from_name"], to_name= details["to_name"], 
        exchange_rate = details["exchange_rate"], bid= details["bid"], ask= details["ask"])
        currency.save()
        print(currency)
        
        return JsonResponse(model_to_dict(currency), safe=False)
    else:
        return JsonResponse(model_to_dict(Currency.objects.last()), safe=False)

