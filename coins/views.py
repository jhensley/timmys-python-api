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

foos = [1, 5, 10, 20, 50]
bars = [1, 2]

@csrf_exempt
def api(request):

    total = float(request.GET.get("total"))
    queryFoos = int(request.GET.get("total").split(".")[1])
    queryBars = int(total)

    response = {
        "total": total, 
        "coins": {
            "foos": _getCurrency(queryFoos, foos),
            "bars": _getCurrency(queryBars, bars)
        }
    }

    return JsonResponse(status=200, data=response)

def _getCurrency(value, bits):

    out = {}
    
    for bit in sorted(bits,reverse=True):
        bitStr = str(bit)
        out[bitStr] = 0
        if value >= bit:
            out[bitStr] = int(value/bit)
            value %= bit
        
    return out
    