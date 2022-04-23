
## Pasos para crear proyecto en Django

- Creamos el entorno virtual y la entramos
```python
#Esto creara una carpeta .env con todos las librerias necesarias
python3 -m venv .env
#Para activar nuestro entorno virtual usuamos
source .env/bin/activate #linux
.env\Scripts\Activate.ps1 #Windows
```
- Procedemos a instalar django en nuestro entorno virtual
```python
python3 -m pip install django~=4.0.0
python3 -m pip install --upgrade pip
```
- Creamos nuestro proyecto
```python
django-admin startproject django_project3 .
#Inicializamos el proyecto 
python manage.py runserver
```

- Creamos una app en nuestro proyecto
```python
python manage.py startapp formulario
#Dentro de nuestro app formulario creamos:
#Archivo: urls.py
#Carpeta: templates
#Carpeta: static
#Agregamos nuestra app a nuestro proyecto en el archivo settings.py, para poder visualizarlo en el admin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'formulario.apps.FormularioConfig' #El nombre FormularioConfig es el que tiene el archivo formulario>apps.py en su clase
]
```

- Migramos nuestrso modelos creados en nuestra app formulario>models.py
```python
python3 manage.py makemigrations formulario 
python3 manage.py migrate
```

- En nuestra app importamos nuestro modelo en el admin.py
```python
from .models import Formula
# Register your models here.
admin.site.register(Formula)
```
- Creamos nuestro super usuario para acceder al admin de python
```python
python3 manage.py createsuperuser
# http://127.0.0.1:8000/
```

```python
from .models import Formula
```

```python
from .models import Formula
```

```python
from .models import Formula
```