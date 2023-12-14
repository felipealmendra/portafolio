from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, FileResponse
from user_agents import parse
import os



def index(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT','')
    ua_object = parse(user_agent_string)
    
    # Verifica si es un dispositivo móvil
    is_mobile = ua_object.is_mobile
    
    # Verifica si es una PC
    is_pc = ua_object.is_pc
    
    print("is_pc:", is_pc)
    
    return render(request,"portafolio/index.html", {'is_mobile': is_mobile, 'is_pc': is_pc})

def download_apk(request):
    apk_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'apk/app-debug.apk')
    response = FileResponse(open(apk_path, 'rb'), as_attachment=True)

    # Agregar un mensaje de éxito a la URL de redirección
    download_status = request.GET.get('download_status', None)
    if download_status == 'success':
        return render(request, 'app_descargada.html', {'message': 'La aplicación ha sido descargada con éxito'})
    
    return response

def mail(request):
    
    user_agent_string = request.META.get('HTTP_USER_AGENT','')
    ua_object = parse(user_agent_string)
    
    # Verifica si es un dispositivo móvil
    is_mobile = ua_object.is_mobile
    
    # Verifica si es una PC
    is_pc = ua_object.is_pc
    
    if request.method=="POST":
        subject=request.POST["name"]
        
        message=request.POST["message"] + " " + request.POST["email"]
        
        email_from=settings.EMAIL_HOST_USER
        
        recipient_list=["correosdjango@gmail.com"]
        
        send_mail(subject, message, email_from, recipient_list)
        
        
        return render(request,"portafolio/sent_mail.html", {'is_mobile': is_mobile, 'is_pc': is_pc})
    
    
    return render(request,"portafolio/sent_mail.html")


def base(request):
    return render(request,"base.html")


def portfolio_mail_view(request):   
    return render(request, 'portafolio/mail_template.html')

def prueba(request):   
    return render(request, 'prueba.html')