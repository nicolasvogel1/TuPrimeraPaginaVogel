# TuPrimeraPaginaVogel

Proyecto web desarrollado con Django utilizando el patrón MVT.

## Funcionalidades

La página permite:

- Crear autores
- Crear posts
- Buscar posts por título

## Cómo probar el proyecto

1. Ejecutar el servidor con:

python manage.py runserver

2. Entrar en el navegador a:

http://127.0.0.1:8000/

3. Usar el menú para:

- Crear un autor
- Crear un post
- Buscar un post

## Panel de administración

Se puede acceder al panel de administración en:

http://127.0.0.1:8000/admin

## Instalación del proyecto

1 Crear entorno virtual

python -m venv venv

2 Activar entorno virtual

venv\Scripts\activate

3 Instalar dependencias

pip install -r requirements.txt

4 Ejecutar servidor

python manage.py runserver