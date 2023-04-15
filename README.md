# Calendar

Creas un directorio y dentro sigues los siguientes pasos:

1. git clone https://github.com/Heaven-sFeel/Calendar.git

2. cd app

3. virtualenv env

4. .env/Scripts/activate.ps1

5. pip install django

6. python manage.py makemigrations

7. python manage.py migrate

8. python manage.py runserver

# Como desplegar Django en Xampp?

1. Instala XAMPP: Descarga e instala XAMPP en tu computadora desde su sitio web oficial.

2. Crea un entorno virtual: Crea un entorno virtual para tu proyecto Django utilizando virtualenv o conda.

3. Instala Django: Instala Django en el entorno virtual que creaste utilizando el comando pip install django.

4. Crea un proyecto Django: Crea un nuevo proyecto Django utilizando el comando django-admin startproject <nombre_del_proyecto>.

5. Configura el proyecto: Abre el archivo settings.py dentro del proyecto Django y agrega la dirección IP y el puerto de la siguiente manera:

ALLOWED_HOSTS = ['192.168.3.100']
DEBUG = False

6. Configura el archivo httpd.conf: Abre el archivo httpd.conf en la carpeta de configuración de Apache y agrega las siguientes líneas al final del archivo:
Alias /static/ "ruta/al/directorio/static/"
<Directory "ruta/al/directorio/static/">
Require all granted
</Directory>

WSGIScriptAlias / "ruta/al/proyecto/wsgi.py"
WSGIPythonPath "ruta/al/proyecto"

<Directory "ruta/al/proyecto">
<Files wsgi.py>
Require all granted
</Files>
</Directory>

7. Crea el archivo wsgi.py: Crea un archivo llamado wsgi.py en el directorio raíz del proyecto Django y agrega el siguiente código:
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<nombre_del_proyecto>.settings')

application = get_wsgi_application()

8. Reinicia Apache: Reinicia el servidor Apache de XAMPP para que se apliquen los cambios.

9. Accede a la aplicación: Accede a tu aplicación Django en tu navegador web utilizando la dirección IP y el puerto especificados en el archivo settings.py.

# Como desplegar la aplicacion web en Apache?

1. Descargar Apache y sus dependencias; instalar las dependencias primero: 
Apache - https://www.apachelounge.com/download/
Dev C++ - https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. Descomprimir el archivo y pegarlo en el disco local.

3. Abrir CMD, buscar la ruta: C:/Apache24/bin/. con el comando (cd) y luego ejecutar los siguientes comandos:
Para instalar el servidor: httpd.exe -k install
Para iniciar el servidor: httpd.exe -k start

Ademas, estan los siguientes comandos:
Para parar el servidor: httpd.exe -k stop
Para reiniciar el servidor: httpd.exe -k resart
