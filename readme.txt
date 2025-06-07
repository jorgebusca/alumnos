Para crear un frontend en Django y Django REST Framework (DRF), puedes seguir estos pasos:
.- creamos un entorno virtual 
	py -m venv venv 

.- ingresamos a la carpeta, de la siguiente manera:
    cd venv
    \venv\cd scripts
    \venv\Scripts\activate
     y se vera asi 
    (venv) C:\wamp64\www\paginas\pagina_modelo\venv\Scripts>
    salen de la carpeta scripts con cd..
    salen de la carpeta venv con cd..
####################################################################################################################################################################

. **Configura tu proyecto Django**:
    Asegúrate de tener Django y Django REST Framework instalados. Si no lo están, instálalos con:
    ```bash
    pip install django 
    ```
####################################################################################################################################################################
. **Crea un proyecto Django**:
    ```bash
    django-admin startproject nombre del projecto 
    cd django_crud  #ingreso al projecto 
    ```

. **Crea una aplicación Django**:
    ```bash
    python manage.py startapp myapp  #creamos la app
    ```

. **Configura `INSTALLED_APPS`**:
    Agrega `myapp` y `rest_framework` en el archivo `settings.py`:
    ```python
    INSTALLED_APPS = [
         ...         
         'myapp',
    ]
    ```
#######################################################################################################################################################################
.-CREAMOS EL FRONT END

<!-- Creamos la Pagina de inicio -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bienvenida</title>
    
</head>
<body>
    <header>
        <h1>Bienvenido a Django </h1>
    </header>
    <main>
        <p>Esta es la pagina de inicio de su aplivcacion. ¡Siéntete libre de explorarlo y personalizarlo!</p>
    </main>
    <footer>
        <p>&copy; 2023 MyApp. Todos los registros Reservados.</p>
    </footer>
</body>
</html>

######################################################################################################################################################################


<!-- Creamos la Pagina de contacto-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contacto</title>
</head>
<body>
    <h1>Contacto</h1>
</body>
</html>

######################################################################################################################################################################


<!-- Creamos la Pagina de usuarios-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuario</title>
</head>
<body>
    <h1>Usuario</h1>
</body>
</html>

######################################################################################################################################################################


<!-- Creamos la Pagina de loguearse-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loguearse</title>
</head>
<body>
    <h1>Loguearse</h1>
</body>
</html>


######################################################################################################################################################################
######################################################################################################################################################################


<!-- Creamos la Pagina de Base-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Base</title>

</body>
</html>


######################################################################################################################################################################

<!-- Creamos la Pagina de registrarse-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrarse</title>
</head>
<body>
    <h1>Registrarse</h1>
</body>
</html>

######################################################################################################################################################################


----------------- CREANDO PAGINAS EN VIEWS --------------------------------

VAMOS A LA CARPETA VIEWS Y CREAMOS UNA FUNCION PORCADA PAGINA 

def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    return render(request, 'contacto.html') 

def usuarios(request):
    return render(request, 'usuarios.html') 

def loguearse(request):
    return render(request, 'loguearse.html')

def registrarse(request):
    return render(request, 'registrarse.html')



######################################################################################################################################################################

----------------- CREANDO PAGINAS EN URL --------------------------------

from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),   
    path('usuarios/', views.usuarios, name='usuarios'),
    path('loguearse/', views.loguearse, name='loguearse'),
    path('registrarse/', views.registrarse, name='registrarse'),     
]
######################################################################################################################################################################
  '''
  ya vimos como creamos las paginas 
  veamos como creamos el formulario de registro
  en views creamos la funcion de Django 
  '''

# para ver como funciona realizamos lo siguiente 

def registrarse(request):
    titulo = "Hola Mundo "
    return render(request, 'registrarse.html', {'miTitulo': titulo})

# y en la pagina html coloco???

  {{titulo}}

# vemos la pagina que nos dice  

# veamos crear un formulario de django importasmos

from django.contrib.auth.forms import UserCreationForm

# y modificamos la funcion asi

def registrarse(request):
    return render(request, 'registrarse.html', {'form': UserCrationForm})

# y en el html llamo a form {{form}} veamos que sucede 


######################################################################################################################################################################

							clase del dia 15/05/2025

######################################################################################################################################################################
'''
creamos la pagina de registro 
ya vimos lo siguiente 
creamos la funcion de la pagina de registro
llamamos a la libreria
'''
from django.contrib.aut.forms import UserCreationForm

def registro(request)	
	return reder(request, 'formulario.html',{
	    'form':UserCreationForm
	})


'''
En el HTML llamamos al form
'''
<main>
 <h1>Registrarse</h1>

      {{form}}
</main>

'''
si vemos en f12 Elementos vemos que solo hay Labels e input 

no hay ningun formulario creado ni tampoco donde enviarlo 
'''
######################################################################################################################################################################
'''
Nosotros podemos crear nuestro formulario y colocarlo en el html
'''
<main>
	
	 <h1>Registrarse</h1>

	<form>

     	 {{form}} #para que el formulario se vea ordenado colocamos {{form.as_p }} y nos muestra mas ordenado el formulario   

	</form>
</main>

'''
creamos el formulario con el action para enviarnos a la pagina de registro 
y agregamos el boton de enviar 
'''

<body>
    {% block content %}
    <main class content>
        <h1>Pagina de Registro</h1>
            
            <form action="{% url 'registrarse' %}" method="post">
            
            {{form}}
            <button type="submit">Registrarse</button>
        </form>
    </main>
    {% endblock %}
</body>

# Ahora tendria que enviarnos los datos del formulario 
# veamos paso a paso el envio 



######################################################################################################################################################################
'''
veamos como hacer que el formulario funcione 
para eso veamos con f12 que el formulario de django no es un formulario sino que es el formato del formulario 
para que sea un formulario en html lo encerramos en la etiqueta "<form></form>"
el form tiene un action para enviar los datos del formulario 
en el html creamos un formulario 

'''
 <h1>Registrarse</h1>
    <form action="{% url 'registrarse' %}" method="POST"> NOS ENVIA LOS DATOS A LA MISMA RUTA O PAGINA
        
        {{form}}
        <button type="submit">Registrarse</button>

    </form>

aca vemos que el formulario esta un  poco desordenado y con {{form.as_p}} lo ordenamos 


''' ahora vemos como nos da un error "La verificación CSRF ha fallado. Solicitud abortada."

pero si agregamos esto: {% csrf_token %} nuestro servidor crea datos seguros para el envio del formulario 
y si lo quieren clonar no van a poder porque no es el mismo token 
vemos esto en pantalla con F12
ahora vuelve a la misma pagina de registro 
######################################################################################################################################################################
''' 
VEAMOS COMO MANEJAMOS LOS DATOS 
Si el método es GET, significa que el usuario está solicitando el formulario para registrarse.
Si el método es diferente (normalmente POST), significa que el usuario ha enviado el formulario con sus datos.
COMPROBAMOS QUE LO ESTAMOS HACIENDO BIEN 
SI LLEGA POR EL METODO GET SIGNIFICA QUE ESTA TRATANDO DE SERVIR ALGO 
ESTA TRATANDO DE VER LA INTERFAST
PERO SI LLEGA POR EL METODO LOST SIGNIFICA QUE ESTA TRATANDO DE PROSESAR DATOS
'''

def registrarse(request):
    if request.method == 'GET':# verificamos si esta solicitando un dato 
        print("enviando formulario")
    else:
        print("obteniendo datos ") 
    return render(request, 'registrarse.html', {'form': UserCreationForm})


# AL ELSE LE AGREGAMOS print(request.POST) ARRIBA DEL PRINT 
# VEMOS CLARA MENTE EN LA TERMINAL QUE NOS ENVIA LOS DATOS 
# CLARAMENTE YA TENEMOS QUE ENVIA LOS DATOS AL SERVIDOR 
# AHI VEMOS EL TOCKEN , Y USERNAME, PASSWORD1 Y PASSWORD2


######################################################################################################################################################################
''' 
AHORA 
vamos a comprobar que las contraseñas sean iguales y registre solo usuarios no duplicados y los guarde en la base de datos
PARA ELLO IMPORTAMOS LOS MODULOS :
'''

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

def registrarse(request):
    if request.method == 'GET':# verificamos si esta solicitando un dato 
        return render(request, 'registrarse.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'], )# creamos una variable con los datos del formulario 
                user.save()  # lo guarda en la base de datos 
                return HttpResponse("<h1>Usuario creado correctamente</h1>")# nos devuelve un mensaje de usuario creado 
            except:
                return HttpResponse("<h1>El usuario ya existe</h1>") 
         return HttpResponse("<h1>Las contraseñas no coinciden </h1>")
'''
ya tenemos la pagina de registro de usuarios funcionando correctamente, si todo va bien ya podemos cargar usuarios en la base de datos 
y nos da error de usuario duplicado, o que los password no coinciden.
la pagina nos sigue redireccionando a la pagina de registrarse
'''

######################################################################################################################################################################

'''
realicemos una pagina de tareas donde registraremos las tareas a realizar en nuestra pagina.
creamos una pagina tareas en views y url
y redireccionaremos de la pagina de registros 
'''

# agregamos despues de render la funcion redirect 
from django.shortcuts import render, redirect

# despues de user.save agregamos

redirect('tareas')

# y retiramos el return, quedaria asi 

def registrarse(request):
    if request.method == 'GET':# verificamos si esta solicitando un dato 
        return render(request, 'registrarse.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
		# ACA DESPUES DE CONFIRMAR LOS Password LE PEDIMOS QUE GUARDE EN LA BASE DE DATOS EL USUARIO
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'], )
                user.save()
                return redirect('tareas')
            except:
                return render(request, 'registrarse.html,{
			'form': UserCreationForm,
			'error': 'El usuario ya existe'
			}) 
        return HttpResponse("<h1>Las contraseñas no coinciden </h1>")

######################################################################################################################################################################
'''
AHORA VAMOS A CREAR UNA SESSION DE USUARIO 
para crear una session de usuario tendremos un modulo o funcion de django que lo hace pòr nosotros 
se llama login y ahora vemos como funciona

'''
from django.contrib.auth import login

def registrarse(request):
    if request.method == 'GET':# verificamos si esta solicitando un dato 
        return render(request, 'registrarse.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
		# ACA DESPUES DE CONFIRMAR LOS USUARIOS LE PEDIMOS QUE GUARDE EN LA BASE DE DATOS EL USUARIO
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'], )
                user.save()
		login(request, user)#aca creamos una kuki para loguearse y la podemos utilizar para saber si esta logueado o que ingrese a una session 
                return redirect('tareas')
            except:
                return render(request, 'registrarse.html,{
			'form': UserCreationForm,
			'error': 'El usuario ya existe'
			}) 
        return HttpResponse("<h1>Las contraseñas no coinciden </h1>")
######################################################################################################################################################################
'''
vamos a crear una except (excepcion) determinada 
vamos a verlo 
'''

from django.db import IntegrityError

def registrarse(request):
    if request.method == 'GET':# verificamos si esta solicitando un dato 
        return render(request, 'registrarse.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:# estamos enviando datos al servidor o base de datos 
		# ACA DESPUES DE CONFIRMAR LOS USUARIOS LE PEDIMOS QUE GUARDE EN LA BASE DE DATOS EL USUARIO
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'], )
                user.save()
		login(request, user)#aca creamos una kuki para loguearse y la podemos utilizar para saber si esta logueado o que ingrese a una session 
                return redirect('tareas')
            except IntegrityError:# si nosotros especificamos el error podriamos seguir creando mas excepciones en la aplicacion 
                return render(request, 'registrarse.html,{
			'form': UserCreationForm,
			'error': 'El usuario ya existe'
			}) 
        return render(request, 'registrarse.html,{
			'form': UserCreationForm,
			'error': 'La contraseña no coinciden '
			}) 

# EN EL HTML CREAMOS QUE NOS MUESTRE EL ERROR DE LA SIGUIENTE MANERA


<main class content>
        <h1>Pagina de Registro</h1>
            {{ error }}
            <form method="POST">
            {%  csrf_token %}
            {{form}}
            <button type="submit">Registrarse</button>
        </form>
    </main>

#
######################################################################################################################################################################
----------------------------------------------------- CREAMOS LA PARTE DE LOGOUT-------------------------------------------------------------------------------------

######################################################################################################################################################################

PARA COLOCAR EL MENU QUE QUERRAMOS DENTRO DE LA SESSION DE LOGUEO.
EN EL BASE.HTML EN LA BARRA DEL MENU LO CONDICIONAMOS DE LA SIGUENTE MANERA

     <header>
        <h1>Insertar logo</h1>
        <nav>
            <ul>                
                <li><a href="{% url 'tareas' %}">Tareas</a></li>
                
                <li><a href="{% url 'contacto' %}">Contacto</a></li>
                

                {% if user.is_authenticated %}

                <li><a href="{% url 'cerrar_sesion' %}">Cerrar Sesion</a></li>

                {% else %}             
                <li><a href="{% url 'loguearse' %}">Loguearse</a></li>           
                <li><a href="{% url 'registrarse' %}">Registrarse</a></li>
                {% endif %}               
            </ul>
        </nav>
        <hr>    
    </header>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------  EN VIEWS  ---------------------------------------------------------------------------------------------
CREAMOS LA FUNSION PARA CERRAR LA SESION 

from django.contrib.aut import login, logout

def cerrar_sesion(request):
    logout(request)# Cierra la sesión del usuario
    return redirect('inicio')# Redirige a la vista de loguearse
    
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------  EN URL    ---------------------------------------------------------------------------------------------

EJECUTAMOS EL PATH PARA EL CIERRE DE SESION

 path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),


######################################################################################################################################################################
----------------------------------------------------- CREAMOS LA PARTE DE LOGUEARSE ------------------------------------------------------------------------------

######################################################################################################################################################################

ASI COMO TENGO UNA FUNCION UserCreationForm TAMBIEN TENGO OTRA QUE SE LLAMA AuthenticationForm

Declaramos la funcion 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


PARA RECORDAR VEMOS TODAS LOS MODULOS Y FUNCIONES DECLARADAS HASTA EL MOMENTO EN VIEWS
En Django, las funciones render y request son fundamentales para manejar las vistas y las solicitudes HTTP

request Es un objeto que representa la solicitud HTTP que se recibe en el servidor. 
Contiene información sobre la solicitud, como los parámetros GET y POST, las cookies, los encabezados, la sesión, entre otros.
Se pasa como argumento a las vistas y permite acceder a los datos enviados por el cliente.



def loguearse(request):
	return render(request, 'loguearse.html')


# EN LA URL VAMOS A CREAR EL PATH

path ('loguearse/', views.loguearse, name = 'loguearse'),

# QUE MAS TENDREMOS QUE CREAR 
# CREAMOS EL HTML 

{% extends 'base.html'%}

<body>
    {% block content %}
    <main class content>
        <h1>Loguearse</h1>
            
    </main>
    {% endblock %}
</body>


# QUE MAS TENDREMOS QUE CREAR 

<li><a href="{% url loguearse %}">Loguearse</a></li>

# UNA VES VISTO QUE FUNCIONA REALIZAMOS LA CREACION DEL FORMULARIO DE LA SIGUIENTE MANERA 


def loguearse(request):
	return render(request, 'loguearse.html', {'form': AuthenticationForm})


#EN EL HTML HACEMOS 
{% extends 'base.html' %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loguearse</title>
</head>
<body>
    {% block content %}

    <h1>Loguearse</h1>   

    {{error}}
    
    <form action='/loguearse/' method="POST">
    
        {% csrf_token %}

        {{form.as_p}}

        <button 
        type="submit">Loguearse
        </button>

        <p>Esta es la pagina de loguearse de su aplicacion. ¡Siéntete libre de explorarlo y personalizarlo!</p>
    
    </form>
    
    {% endblock content %}
    
</body>
</html>
# ACA VEMOS LOS DATOS QUE NOS ENVIA LA PAGINA 

def loguearse(request):
	if request.method == 'GET':# verificamos si esta solicitando un dato 
        	return render(request, 'loguearse.html', {'form': AuthenticationForm})· si el metodo es GET enviamos el formulario 
    else:
	print(request.POST
	return render(request, 'loguearse.html', {'form': AuthenticationForm}) # sino es GET significa que nos estan enviando datos 

#PARA AUTENTICAR LOS DATOS IMPORTAMOS Autenticate LO UTILIZAMOS EN EL ELSE

from django.contrib.aut import login, logout, Autenticate
------------------------------------------------------------------------------------------------------------------------------------------------------------------

CAMBIAMOS EL ELSE
else:
	user=autenticate(request, username=request.POST['username'],
		password=request.POST['password1']
	if user is none:# si el usuario no existe enviale este error 
	    return render(request, 'loguearse.html', {
	      'form': AuthenticationForm
	      'error': 'Usuario o Contraseña incorrecta'
	})
        else: # si el usuario existe envialo a la pagina de tareas y guarda su sesion
	     login(request, user)
             return redirect('tareas')


#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

####################################################################################################################################################################
----------------------------------------------------- Este es el Views Completo-------------------------------------------------------------------------------------

#####################################################################################################################################################################
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def contacto(request):
    return render(request, 'contacto.html') 

def tareas(request):
    return render(request, 'tareas.html') 

def loguearse(request):
    if request.method == 'GET':
        return render(request, 'loguearse.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(request, 
            username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'loguearse.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos',
                })
        else:
            login(request, user)# Inicia sesión al usuario
            return redirect('tareas')# Redirige a la vista de loguearse

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'], )
                user.save()# Guarda el usuario en la base de datos
                login(request, user)# Inicia sesión automáticamente al usuario
                return redirect('tareas')# Redirige a la vista de loguearse
            except IntegrityError:
                # Si el usuario ya existe, muestra un mensaje de error
                return render(request, 'registrarse.html', {
                'form': UserCreationForm,
                'error': 'El usuario ya existe',
                }) 
        return render(request, 'registrarse.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden',
                }) 
        
def cerrar_sesion(request):
    logout(request)# Cierra la sesión del usuario
    return redirect('inicio')# Redirige a la vista de loguearse
    


    



######################################################################################################################################################################
----------------------------------------------------- CREAMOS INGRESO AL ADMIN DE DJANGO ------------------------------------------------------------------------

######################################################################################################################################################################

VAMOS A CREAR UN SUPER USUARIO A LA ADMINISTRACION DE DJANGO en el terminal

py manage.py createsuperuser

AHORA NOS PIDE QUE INGRESEMOS EL USUARIO (admin) DAMOS ENTER
NOS PIDE UN CORREO, LO INGRESAMOS buscajorge@gmail.com
Y NOS PIDE LA CONTRASEÑA (admin)
REPETIMOS LA CONTRASEÑA (admin)

INGRESAMOS Y VEMOS LAS TABLAS CREADAS Y LOS USUARIOS CREADOS 

PARA QUE MI TABLA LA PUEDA VER EN EL PANEL ADMIN 
VAMOS AL ARCHIVO admin.py

IMPORTAMOS

from .models import tareas, usuarios

admin.site.register(tareas)
admin.site.register(uasuarios)

ORM (OBJECT, RELATIONAL, MAPPING)


     

######################################################################################################################################################################
----------------------------------------------------- CREAMOS BD EN MODELS.PY-------------------------------------------------------------------------------------

######################################################################################################################################################################

DJANGO YA VIENE CON MODULOS QUE NOS PERMITEN ADMINISTRAR ESTA BASE DE DATOS
DJANGO VIENE CON UN : ORM (OBJECT RELATIONAL MAPPING) SON COMO EL CRUD  
TAMBIEN PODEMOS INTERACTUAR CREANDO NUESTRA PROPIAS TABLAS EN LA BASE DE DATOS

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class tareas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10 , decimal_places=2)
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)# combinamos el usuario con la tabla y cuando lo borramos, borramos las tareas en cascada
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.precio}"
    
-------------------------------------------------------------  PARA CREARLOS EN LAS BASES DE DATOS HACEMOS  ----------------------------------------------------------

CTRL + C # para salir del servidor y ejecitamos 


py manage.py makemigrations #genera un archivo en migrations con la table en la base de datos

ERRORS:
myapp.tareas.imagen: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".#esto es para ingresar imagenes en la BD


py manage.py migrate  #genera en admin la tabla (iniciamos el servidor con )


py manage.py runserver


IMPORTANTE: UNA VES CREADA LAS BASES DE DATOS Y LOS FORMULARIOS PUEDO BORRAR TODO LO QUE ESTA DENTRO DE MIGRATIOS MENOS EL ININT PARA SOLUCIONAR INCONVENIENTES Y VOLVER A EMPEZAR CON LAS BASES DE DATOS !!!!! NUNCA HACERLO CON BASES DE DATOS FUNCIONANDO SIN HACER YB BACKUP DE LAS MISMAS !!!!!!!

######################################################################################################################################################################
----------------------------------------------------- VEMOS COMO CREAMOS LAS TABLAS PARA CARGAR DATOS EN ADMIN -------------------------------------------------------

######################################################################################################################################################################
TENEMOS QUE DARLE ACCESO AL PANEL PARA QUE SE CREE EN ADMIN

# VOY A ADMIN.PY 


from .model import tareas

# MOSTRAMOS ESTO PRIMERO QUE ES LA TAREA CREADA EN MODEL 

admin.site.register(tareas)

# si lo que quiero es mostrar la fecha en el formulario de administrador, hago lo siguiente

class tareaAdmin(admin.ModelAdmin):	
	readonly_fields = ("fecha_creacion",) # me muestra la fecha de creadcion 

# MOSTRAMOS ESTO PRIMERO 
admin.site.register(tareas, tareaAdmin)



######################################################################################################################################################################
----------------------------------------------------- VEMOS COMO CREAMOS FORMULARIO PARA CREAR TAREAS -------------------------------------------------------

######################################################################################################################################################################

EN HTML CREAMOS EL ARCHIVO CREAR_TAREAS.HTML

{% extends 'base.html' %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loguearse</title>
</head>
<body>
    {% block content %}

    <h1>Crear Tareas</h1>   

   
    
    {% endblock content %}
    
</body>
</html>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

en views.py creamos 

def crear_tareas(request):
    return render(request, 'crear_tareas.html')


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

en url.py creamos 

path(crear_tareas/, views.crear_tareas, name= 'crear_tareas')

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


######################################################################################################################################################################
----------------------------------------------------- VEMOS COMO CREAMOS FORMULARIO CREADO PÒR NOSOTROS  -------------------------------------------------------

######################################################################################################################################################################

VAMOS A MIAPP Y CREAMOS UN ARCHIVO 

formulario.py 

y dentro 

from django.forms import ModelForm   # Esta clase nos permite extenderla creando nuestra clase
from .models import Tareas

class TareasForm(ModelForm):
	class Meta:
		model = Tareas
		fields = ['nombre', 'descripcion', 'precio', 'imagen']#NOMBRO LOS CAMPOS QUE QUIERO UTILIZAR 


          AHORA TENGO UN FORMULARIO PARA ENVIAR AL FRONT END

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

VAMOS AL VIEWS EN LA FUNSION CREAR_TAREAS

 IMPORTAMOS EL FORMULARIO QUE ACABAMOS DE CREAR 

def crear_tareas(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html',{
            'form': TareasForm,
	})
    else:
        # Aquí puedes agregar la lógica para crear una tarea
        # Por ejemplo, guardar la tarea en la base de datos
        return redirect('tareas')# Redirige a la vista de tareas    
    
AHORA YA TENEMOS UN FORMULARIO PARA LLAMARLO DESDE HTML


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


VAMOS A CREAR TAREAS.HTML Y LLAMAMOS AL FORMULARIO 


 {% block content %}

    <h1>Crear Tareas</h1>   
   <form action = "/crear_tareas/" method = "POST">

      {% csrf_token %}
      {{form}}

       <button>
            GUARDAR
       </button>
   </form>
   
    
    {% endblock content %}


SI VOY A LA PAGINA TENDRIA que tener el formulario creado 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
VAMOS AL VIEWS EN LA FUNSION CREAR_TAREAS GRABAMOS EN LA BASE DE DATOS


def crear_tareas(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html',{
            'form': TareasForm,
        })
	
    else:
        form = TareasForm(request.POST)
        print(form)
        
        return render(request, 'crear_tarea.html',{
            'form': TareasForm,
        })# Redirige a la vista de tareas    
    
#AHORA VEMOS COMO EL FORMULARIO SE MUESTRA EN LA TERMINAL

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
VAMOS A CREAR EN EL ADMIN  O BASE DE DATOS 


 else:
        form = TareasForm(request.POST)
	nueva_tarea = form.save(commit =False) # esto lo guardaria como una instancia en la base de datos 
	nueva_tarea.user = request.user
        print(nueva_tarea)# Primero hacemos que lo muestre y despues lo borramos 
        nueva_tarea.save()
        return redirect(request, 'tarea.html')# Redirige a la vista de tareas     
       
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

VIEWS TERMINADO 

def crear_tareas(request):
    if request.method == 'GET':
        return render(request, 'crear_tareas.html',{
            'form': TareasForm,
	})
    else:
        try:
            form = TareasForm(request.POST)
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
        
           
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------  
VAMOS A CREAR LA PAGINA DE LAS TAREAS.HTML 

LO PRIMERO QUE TENDREMOS QUE SABER ES QUE TENDREMOS QUE MOSTRAR LA TAREA EN LA PAGINA
LO SEGUNDO SERIA RECORRER TODAS LAS TAREAS QUE ESTAN EN LA BASE DE DATOS
PARA ELLO CONFORMAMOS UN PARA :

{% extends 'base.html' %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tareas</title>
</head>
<body>
    {% block content %}
    <h1>Tareas</h1>
    <p>Esta es la pagina de tareas de su aplicacion. ¡Siéntete libre de explorarlo y personalizarlo!</p>
   <ul>
        {% for tarea in tareas %}
            <li>
                <h2>{{ tarea.nombre }}</h2>
                <p>{{ tarea.descripcion }}</p>
                <p>{{ tarea.usuario.username }}</p>
                <p>{{ tarea.imagen }}</p>                
            </li>
        {% empty %}
            <li>No hay tareas disponibles.</li>
        {% endfor %}
   </ul>
    {% endblock content %}


    <h1>Tareas</h1>
</body>
</html>
	

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                     CREAMOS LA FUNCION TAREAS DE VIEWS
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def tareas(request):
    Tarea = Tareas.objects.all()
    #Tarea = Tareas.objects.filter(usuario=request.user) # Filtra las tareas por el usuario logueado
    return render(request, 'tareas.html', {'tareas': Tarea})

# AHI NOS MUESTRA LOS DATOS QUE QUERRAMOS RECORRER

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREAREMOS UNA TABLA PARA MOSTRAR TODOS LOS DATOS EN TAREAS.HTML


{% extends 'base.html' %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tareas</title>
</head>
<body>
    {% block content %}
    <h1>Tareas</h1>
    <p>Esta es la pagina de tareas de su aplicacion. ¡Siéntete libre de explorarlo y personalizarlo!</p>
    <table class="table">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Usuario</th>
            <th>Imagen</th>
            <th>Acciones</th>
        </tr>
        {% for tarea in tareas %}
        <tr>
            <td>{{ tarea.id }}</td>
            <td>{{ tarea.nombre }}</td>
            <td>{{ tarea.descripcion }}</td>
            <td>{{ tarea.usuario.username }}</td>
	    <td><img src="{% static imagen %  }}" alt="{{ tarea.imagen }}" style="width: 100px; height: auto;"></td># Traemos la imagen desde la carpeta static
            <td>{{ tarea.imagen }}</td>
        </tr>
        {% empty %}
        <tr>
            <td colspan="5">No hay tareas disponibles.</td>
        </tr>
        {% endfor %}
    </table>
    {% endblock content %}


    <h1>Tareas</h1>
</body>
</html>


--------------------------------------------------------------------------------------------------------------------------------------------------------------------

A ESTA TABLA LE AGREGO LOS BOTONES MODIFICAR Y BORRAR PARA CADA REGISTRO 

             <td>
                <a href="{% url 'modificar_tarea' tarea.id %}" class="btn btn-primary">Modificar</a>
                <a href="{% url 'borrar_tarea' tarea.id %}" class="btn btn-danger">Borrar</a>
            </td>
                                           
-------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
CREAMOS EL HTML MODIFICAR_TAREA.HTML

{% extends 'base.html' %}

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Modificar Tarea{% endblock %}</title>
    
</head>
<body>
    {% block content %}
    <h1>Modificar Tarea</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar Cambios</button>
        <button><a href="{% url 'tareas' %}">Cancelar</a></button>
    </form>
    {% endblock %}
</body>
</html>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

CREAMOS LA URL 

    path("modificar_tarea/<int:tarea_id>/", views.modificar_tarea, name="modificar_tarea"),# Ruta para modificar una tarea existente, recibe el ID de la tarea como parámetro
    path("borrar_tarea/<int:tarea_id>/", views.borrar_tarea, name="borrar_tarea"),# Ruta para borrar una tarea, recibe el ID de la tarea como parámetro


----------------------------------------------------------------------------------------------------------------------------------------------------------------------

EN VIEWS CARGAMOS EL MODIFICAR_TAREAS, LISTAR_TAREAS, Y BORRAR_TAREAS
            
def modificar_tareas(request, tarea_id):
    tarea = get_object_or_404(Tareas, pk=tarea_id)  # Obtiene la tarea por su ID    
    modificar = Tareas.objects.get(id=tarea_id)  # Obtiene la tarea a modificar
    if request.method == 'POST':
        form = TareasForm(request.POST, instance=modificar)  # Pasa los datos del formulario
        if form.is_valid():  # Verifica si el formulario es válido
            form.save() #Guardar los cambios en la tarea
            return redirect('tareas')
        else:            
            return render(request, 'modificar_tareas.html', {
            'form': form,
            'tarea': tarea,
            'error': 'Error al modificar la tarea',
        })
    else:
        form = TareasForm(instance=modificar)# Crea un formulario con los datos actuales de la tarea
        return render(request, 'modificar_tareas.html', {
        'form': form,
        'tarea': tarea,
    })  # Renderiza la plantilla de modificación de tareas con el formulario y la tarea modificar



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
def lista_tareas(request):
    tareas = Tareas.objects.all()  # Obtiene todas las tareas de la base de datos
    return render(request, 'lista_tareas.html', {'tareas': tareas})  # Renderiza la plantilla con las tareas


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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Creamos el HTML BORRAR_TAREA.HTML

{% extends 'base.html' %}
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Eliminar Tarea{% endblock %}</title>
    
</head>
<body>
    {% block content %}
    <h1>Eliminar Tarea</h1>
    <p>¿Estás seguro de que deseas eliminar la tarea </p>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Borrar</button>
        <button><a href="{% url 'tareas' %}">Cancelar</a></button>
    </form>
    {% endblock %}
</body>
</html>          


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------





                        