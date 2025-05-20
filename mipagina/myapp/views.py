from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def index(request):
    return render(request, "index.html")


def contacto(request):
    return render(request, "contacto.html")


def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:  # comparo si los password son iguales
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])  # traigo los datos del formulario
                user.save()  # aca estoy guardando en la BD
                login(request, user)# creando un login                
                return redirect('tareas')
            except:
                return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
        })            
        return render(request, 'registrarse.html', {
                    'form': UserCreationForm,
                    'error': 'Las contraseñas no coinciden'
        }) 

    
def cerrar_sesion(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect( "index")

   
def loguearse(request):
    if request.method == 'GET':  # verificamos si esta solicitando un dato      
        return render(request, "loguearse.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],
            password=request.POST['password'])# si el usuario existe me lo devuelve y si no lo devuelve vacion
        if user is None:  # si el usuario no existe o esta vacio enviale este error 
            return render(request, 'loguearse.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña incorrecta',
            })
        else:
            login(request, user)
            return redirect('tareas')


def tareas(request):
    return render(request, "tareas.html")

