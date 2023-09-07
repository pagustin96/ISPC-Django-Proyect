from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def get_data(request):
    data = {
        "message": "Hello from Django!",
        "data": ["item1", "item2", "item3"]
    }
    return JsonResponse(data)
