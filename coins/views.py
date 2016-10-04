# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# We're using Foobar Currency, where there are 100 Foos to one Bar and
# the denominations are:
#	 1  Foo
#    5  Foos
#    10 Foos
#    20 Foos
#    50 Foos
#    1  Bar
#    2  Bars

@csrf_exempt
def api(request):
    response = {}

    return JsonResponse(status=200, data=response)