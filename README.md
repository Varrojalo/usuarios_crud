# Usuarios CRUD
Este es mi version del proyecto que se nos dio como tarea para crear en el bootcamp Fullstack Python Flask de Coding Dojo (actualmente Skillnest) en noviembre de 2024.

En mi caso decidí hacer uso de TailwindCSS para la visualización más moderna del proyecto (cosa que no era necesaria para completarlo.

## Requisitos

- [Python 3.13](https://www.python.org/downloads/)
- [MySQL 8](https://dev.mysql.com/downloads/) corriendo en local
- Pipenv (se instala con `pip install pipenv`)

## Cómo levantarlo

1. Abre una terminal en una carpeta local.
2. Clona el repositorio en una carpeta local con ```git clone https://github.com/Varrojalo/usuarios_crud.git``` en la terminal
3. Entra a la carpeta del proyecto con ```cd usuarios_crud```
4. Crea la BD y los datos de prueba usando```mysql -u root -p < flask_app/bd/db_usuarios.sql```
5. Copia `.env.example` como `.env` y reemplaza los valores que dicen *"cambia-esta-clave"* por tu clave de MySQL y una clave de Flask generada.
6. Instala las dependencias ```pipenv install```
7. Levanta el servidor ```pipenv run python server.py```
8. Abre "http://127.0.0.1:5000" en el navegador.

> **NOTA:** el script del paso 3 ejecuta `DROP TABLE IF EXISTS usuarios`. Si ya tienes una base llamada `esquema_usuarios`, perderás esa tabla.
