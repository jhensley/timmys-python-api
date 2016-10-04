from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

treatments = {
    "doctor": "flu shot",
    "vet": "shots and a chew toy"
}

@csrf_exempt
def api(request):
    r = json.loads(request.body)
    response = {
        "greeting": "Hi " + r["name"] + "!",
        "patients": _mapPatientsToTreatment(r["patients"], r["job"])
    }

    return JsonResponse(status=200, data=response)

def _mapPatientsToTreatment(patients, job):
    treatment = treatments[job.lower()]
    treatmentToPatients = []

    for patient in patients:
        treatmentToPatients.append({
            "patient": patient,
            "treatment": treatment
        })

    return treatmentToPatients