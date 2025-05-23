from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("contacto/", views.contacto, name="contacto"),
    path("registrarse/", views.registrarse, name="registrarse"),
    path("loguearse/", views.loguearse, name="loguearse"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("tareas/", views.tareas, name="tareas"),
    path("crear_tareas/", views.crear_tareas, name="crear_tareas"),
]
