from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
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
    path("modificar_tarea/<int:tarea_id>/", views.modificar_tarea, name="modificar_tarea"),
    path("eliminar_tarea/<int:tarea_id>/", views.eliminar_tarea, name="eliminar_tarea"),
    #path("task_detail/<int:tarea_id>/", views.task_detail, name="task_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)