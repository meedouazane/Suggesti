from django.http import JsonResponse
from rest_framework.decorators import api_view
from .similarity import check
import json



@api_view(['POST'])
def similarity(request):
    """
    Define an API view for similarity calculation
    Return the suggestions as a JSON response
    """
    if request.method == 'POST':
        name = request.data.get('name')
        if not name:
            raise ValueError("Missing 'name' in request data")
        try:
            seguelist = check(name)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Error finding suggestions: {str(e)}"}, status=500)
        return JsonResponse({"suggestions": seguelist})
    # Return an error if the request method is not POST or request is invalid
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@api_view(['POST'])
def dialogflow_webhook(request):
    """
    Define an API view to handle Dialogflow webhook requests
    Return the suggestions in the 'fulfillmentText' field for Dialogflow's response
    """
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        name = req.get('queryResult').get('queryText')
        if not name:
            raise ValueError("Missing 'name' in request data")
        seguelist = check(name)
        seguelist = ", ".join(seguelist)
        return JsonResponse({
            "fulfillmentText": f"Here are some similar movies: {seguelist}",
        })
    # Return an error if the request method is not POST or request is invalid
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)