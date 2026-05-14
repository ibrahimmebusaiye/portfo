from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage
from django.core.mail import send_mail

from django.contrib.auth.models import User

def create_admin():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="Ibytech001",
            email="ibytechsolution01@gmail.com",
            password="Ibytech184943*#ACF"
        )

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # 1. Save to database (your existing system)
        ContactMessage.objects.create(
            name=data.get("name"),
            email=data.get("email"),
            subject=data.get("subject"),
            message=data.get("message"),
        )

        # 2. Send email notification (NEW ADDITION)
        send_mail(
            subject=f"New Contact Message: {data.get('subject')}",
            message=f"""
You received a new message from your website:

Name: {data.get('name')}
Email: {data.get('email')}
Subject: {data.get('subject')}
Message:
{data.get('message')}
            """,
            from_email="ibytechsolution01@gmail.com",   # change this
            recipient_list=["ibytechsolution01@gmail.com"],  # your receiving email
            fail_silently=False
        )

        return JsonResponse({"message": "Success"})

    return JsonResponse({"error": "Only POST allowed"})