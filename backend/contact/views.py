from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ContactMessage
from django.core.mail import send_mail

@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Save message
            ContactMessage.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                subject=data.get("subject"),
                message=data.get("message"),
            )

            # Send email (safe)
            send_mail(
                subject=f"New Contact Message: {data.get('subject')}",
                message=f"""
Name: {data.get('name')}
Email: {data.get('email')}
Subject: {data.get('subject')}

Message:
{data.get('message')}
                """,
                from_email="ibytechsolution01@gmail.com",
                recipient_list=["ibytechsolution01@gmail.com"],
                fail_silently=True
            )

            return JsonResponse({"message": "Success"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)