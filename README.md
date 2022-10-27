# Proyecto web Django con Python
Versión desarrollada en Python 3.10.6.

Esta aplicación permite administrar un sitio para guardar información en una base de datos. En ellas se podrá:
- Agregar nuevas instancias de tres modelos diferentes: Pacientes, Funcionarios y Consultas médicas.
- Realizar búsquedas en la base de datos: de pacientes (por nombre), de funcionarios (por su número de funcionario) y de consultas médicas (por especialidad).
- Visualizar la información generada en la base de datos en forma de lista para cada uno de los tres modelos.

##Pasos para su instalación:

1° Clonar el proyecto desde GitHub: `git clone https://github.com/javierdeus04/proyecto-final-coderhouse.git .` o descargar el archivo comprimido que contiene la carpeta del proyecto.

2° En la ruta correspondiente a la carpea del proyecto:
- Realizar las migraciones: `python manage.py migrate`
- Correr el servidor: `python manage.py runserver`

3° En el navegador ir al localhost http://127.0.0.1:8000/ para confirmar que la aplicación funciona correctamente.

##Recorriendo la app:
- Ingresar a http://127.0.0.1:8000/admin/ para acceder al sitio de administrador
- Ingresar a http://127.0.0.1:8000/ppal/ para acceder al menú principal





  

