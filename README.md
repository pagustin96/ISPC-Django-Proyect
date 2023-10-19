# GESTION DE INSTITUCIONES EDUCATIVAS

Aplicacion desarrollada con Python, MySQL, Django, Django Restframework.
Deployada en Pythonanywhere
## Requisitos para correr el proyecto local:
IMPORTANTE!!
Antes de correr el proyecto de forma local se debe crear la base de datos con el nombre ispc

A. Entorno de Desarrollo
   1. Setear VirtualEnv:<br>
      `python -m virtualenv venv`
   2. Activar VirtualEnv:<br>`*correr archivo* -> \path\to\venv\Scripts\Activate.bat` o `.\env\Scripts\activate `
   3. Instalar las dependencias:<br>`pip install django djangorestframework pandas SQLAlchemy django-cors-headers djangorestframework-simplejwt coreapi mysqlclient sqlalchemy_utils python-dotenv`
   4. Configurar variables de entorno HOST, USER, PASSWORD, DB, DIALECT creando el archivo .env siguiendo el .env.example en el repositorio local

B. Conexion con MySQL:
   1. En ISPC-Django-Proyect/djangoproject/djangoproject/settings.py configurar los datos de la base de datos MySQL:
        ![image](https://github.com/pagustin96/ISPC-Django-Proyect/assets/105244530/64dc0ae5-1ec2-4829-a209-d7430907e2f4)



C. Iniciar servidor local  
   1. Posicionarse en ISPC-Django-Proyect y correr el comando "python manage.py makemigrations" luego "python manage.py migrate" y por ultimo "python manage.py runserver"
   2. Abrir http://127.0.0.1:8000/

Diagrama de Entidades
![Imagen de WhatsApp 2023-10-10 a las 21 05 31_5d9178a6](https://github.com/pagustin96/ISPC-Django-Proyect/assets/105244530/c7d94e45-6f0c-4516-a68c-290bf55416a6)
