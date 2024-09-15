from django.http import JsonResponse
from rest_framework.decorators import api_view
from .similarity import check
import json



@api_view(['POST'])
def similarity(request):
    name = request.data.get('name')
    seguelist = check(name)
    return JsonResponse({"suggestions": seguelist})


@api_view(['POST'])
def dialogflow_webhook(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        name = req.get('queryResult').get('queryText')
        seguelist = check(name)
        seguelist = ", ".join(seguelist)
        return JsonResponse({
            "fulfillmentText": f"Here are some similar movies: {seguelist}",
        })
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)