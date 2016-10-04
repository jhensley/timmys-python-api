# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api(request):
    r = json.loads(request.body)
    response = {}

    return JsonResponse(status=200, data=response)