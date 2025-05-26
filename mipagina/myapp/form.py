
from django.forms import ModelForm 
# Esta clase nos permite extenderla creando nuestra clase
from .models import Tareas

class TareasForm(ModelForm):
	class Meta:
		model = Tareas
		fields = ['nombre', 'descripcion', 'precio', 'imagen']
#NOMBRO LOS CAMPOS QUE QUIERO UTILIZAR 