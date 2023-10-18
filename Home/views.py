from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Index
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        index = Index(name=name, email=email, subject=subject, message=message, date=datetime.today())
        index.save()
        messages.success(request, "Your message has been sent")
    return render(request, 'index.html')