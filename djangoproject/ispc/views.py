from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages 
from djangoproject.djangoproject.models import Barrios,Campus,Carreras,Ciudades, Paises,Personas,PersonasTitulaciones,Provincias,TiposPersona,Titulaciones
from django.http import JsonResponse

# IMPORTADO
from .forms import Personas
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate

def login_view(request):
    
    if request.user.is_authenticated:
            return redirect('template-home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,'¡Operación completada con éxito!')
            return JsonResponse({'mensaje':'ingreso correctamente'})
        else:
            messages.error(request, 'Acceso denegado')
        
    return JsonResponse({"Ingreso correctamente"})

def logout_view(request): 
    logout(request)
    JsonResponse({'message':'Has cerrado sesion'})
    return redirect('template-login')

def registro(request):
    if request.user.is_authenticated:
            return redirect('template-home')
     
    form = Personas(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        email= form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username,email,password)
        if user:
            login(request,user)

            JsonResponse({'message':'Usuario creado exitosamente'})
            # messages.success(request,'Usuario creado existosamente') MENSAJE QUE SALE EN LA PAG
            # return redirect('template-home') PARA REEMPLAZAR con template de ANGULAR

    return JsonResponse({'form': form})