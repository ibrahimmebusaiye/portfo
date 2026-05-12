from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        ContactMessage.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            subject=data.get("subject"),
            message=data.get("message"),
        )

        return JsonResponse({"message": "Success"})

    return JsonResponse({"error": "Only POST allowed"})