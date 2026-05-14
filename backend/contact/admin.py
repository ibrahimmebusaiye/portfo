from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactMessage

admin.site.register(ContactMessage)

from django.contrib.auth.models import User

def create_admin():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="Ibytech001",
            email="ibytechsolution01@gmail.com",
            password="Ibytech184943*#ACF"
        )