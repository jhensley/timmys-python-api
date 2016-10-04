# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api(request):
    response = {}

    return JsonResponse(status=200, data=response)