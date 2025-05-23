from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from .form import TareasForm
from .models import Tareas
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
    if request.method == 'GET':# verificamos si esta solicitando un dato 
        return render(request, 'loguearse.html', {
            'form': AuthenticationForm
            })  #si el metodo es GET enviamos el formulario 
    usuario = authenticate(request, username=request.POST['username'],
    password=request.POST['password'])# verificamos si el usuario existe
    if usuario is None:# si el usuario existe lo logueamos 
        return render(request, 'loguearse.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrectos',
        })
    login(request, usuario)
    return redirect('tareas')
           

def tareas(request):
    tareas = Tareas.objects.all() # traigo todas las tareas 
    return render(request, "tareas.html", {
        'tareas': tareas,
    }) # renderizo la plantilla tareas.html y le paso las tareas que traje de la base de datos


def crear_tareas(request):
    if request.method == 'GET':
        return render(request, 'crear_tareas.html',{
            'form': TareasForm,
	})
    else:
        form = TareasForm(request.POST)
        nueva_tarea = form.save(commit=False) # esto lo guardaria como una instancia en la base de datos 
        
        nueva_tarea.usuario = request.user # este es el usuario de la tares 
        nueva_tarea.save()
        return render(request, 'crear_tareas.html',{
            'form': TareasForm(),
        })# Redirige a la vista de tareas    