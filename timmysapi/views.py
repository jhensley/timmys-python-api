from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def people(request):
    r = json.loads(request.body)
    response = {}

    return JsonResponse(status=200, data=response)