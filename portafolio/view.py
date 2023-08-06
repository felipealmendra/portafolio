from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings




def index(request):
    return render(request,"portafolio/index.html")

def mail(request):
    if request.method=="POST":
        subject=request.POST["name"]
        
        message=request.POST["message"] + " " + request.POST["email"]
        
        email_from=settings.EMAIL_HOST_USER
        
        recipient_list=["correosdjango@gmail.com"]
        
        send_mail(subject, message, email_from, recipient_list)
        
        return render(request,"portafolio/sent_mail.html")
    
    return render(request,"portafolio/sent_mail.html")


def base(request):
    return render(request,"base.html")


def portfolio_mail_view(request):   
    return render(request, 'portafolio/mail_template.html')

def prueba(request):   
    return render(request, 'prueba.html')