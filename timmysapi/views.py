from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

treatments = {
    "doctor": "flu shot",
    "vet": "shots and a chew toy"
}

@csrf_exempt
def people(request):
    r = json.loads(request.body)
    response = {}

    return JsonResponse(status=200, data=response)