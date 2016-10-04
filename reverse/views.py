# -*- coding: utf-8 -*-
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import math

@csrf_exempt
def api(request):
    response = {
        "reversed": _reverseInput(request.GET.get("input"))
    }

    return JsonResponse(status=200, data=response)

def _reverseInput(input):
    reversed = input[::-1]
    
    try:
        testFloat = float(reversed)
        if not math.isnan(testFloat):
            reversed = float(reversed)
    except:
        pass

    return reversed