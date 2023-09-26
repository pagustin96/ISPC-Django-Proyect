
# proyecto-ispc

## Requisitos para correr el proyecto local:
IMPORTANTE!!
Antes de correr el proyecto de forma local se debe crear la base de datos con el nombre ispc

A. Entorno de Desarrollo
   1. Setear VirtualEnv:<br>
      `python -m venv env`
   2. Activar VirtualEnv:<br>`*correr archivo* -> \path\to\venv\Scripts\Activate.bat`
   3. Instalar las dependencias:<br>`pip install django djangorestframework pandas SQLAlchemy django-cors-headers djangorestframework-simplejwt coreapi mysqlclient SQLAlchemy-Utils`
   4. Configurar variables de entorno HOST, USER, PASSWORD, DB, DIALECT creando el archivo .env siguiendo el .env.example en el repositorio local

B. Conexion con MySQL:
   1. En ISPC-Django-Proyect/djangoproject/djangoproject/settings.py configurar los datos de la base de datos MySQL:
        ![image](https://github.com/pagustin96/ISPC-Django-Proyect/assets/105244530/64dc0ae5-1ec2-4829-a209-d7430907e2f4)



C. Iniciar servidor local  
   1. Posicionarse en ISPC-Django-Proyect y correr el comando "python manage.py makemigrations" luego "python manage.py migrate" y por ultimo "python manage.py runserver"
   2. Abrir http://127.0.0.1:8000/
   
