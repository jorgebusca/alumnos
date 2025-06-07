from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from .form import TareasForm
from .models import Tareas
# Create your views here.


def index(request):
    tarea= Tareas.objects.all()
    return render(request, "index.html", {"tarea": tarea})


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
        try:
            form = TareasForm(request.POST, request.FILES)
            if form.is_valid():  # Verifica si el formulario es válido                
                nueva_tarea = form.save(commit=False) # esto lo guardaria como una instancia en la base de datos 
                nueva_tarea.usuario = request.user # este es el usuario de la tares 
                nueva_tarea.save()
                return render(request, 'crear_tareas.html',{
                    'form': TareasForm,
                    'mensaje': 'Tarea creada correctamente',
                })
        except ValueError:
            return render(request, 'crear_tareas.html',{
                'form': TareasForm,
                'error': 'Error al crear la tarea',     
            })# Redirige a la vista de tareas        


def modificar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, id=tarea_id)  # Obtiene la tarea específica por id
    modificar= Tareas.objects.get(id=tarea_id)  # Obtiene la tarea para modificarla
    if request.method == 'POST':
        form = TareasForm(request.POST, instance=modificar)  # Crea un formulario con los datos de la tarea
        if form.is_valid():
            form.save()  # Guarda los cambios en la tarea
            return redirect('tareas')  # Redirige a la vista de tareas
        else:
            return render(request, 'modificar_tarea.html', {
                'form': form, 
                'tarea': tarea, 
                'error': 'Error al modificar la tarea'})    
    else:
        form = TareasForm(instance=modificar)  # Crea un formulario con los datos actuales de la tarea
        return render(request, 'modificar_tarea.html', {'form': form, 'tarea': tarea}) # de tareas con el formulario y la tarea modificar


def eliminar_tarea(request, tarea_id):
    tareas= get_object_or_404(Tareas, id=tarea_id)  # Obtiene la tarea específica por id
    tareas= Tareas.objects.get(id=tarea_id)
    if request.method == 'POST':
        form = TareasForm(request.POST, instance=tareas)  
        if form.is_valid():
            tareas.delete()# Elimina la tarea de la base de datos
            return redirect('tareas')  # Redirige a la vista de tareas
        else:
            return render(request, 'eliminar_tarea.html', {
                'form': form, 
                'tarea': tareas, 
                'error': 'Error al Eliminar la tarea'})   
    else:
        form = TareasForm(instance=tareas)  # Inicializa 'form' aquí   
        return render(request, 'eliminar_tarea.html', {'form': form})  # Renderiza la plantilla con las tareas
