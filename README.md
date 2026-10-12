# Usuarios CRUD
Es mi versión del proyecto que se nos dio como tarea en el bootcamp Fullstack Python Flask de Coding Dojo (actualmente Skillnest) en noviembre de 2024. Es un CRUD de usuarios con listado, creación, edición y eliminación.

## Notas de arquitectura
En mi caso decidí usar TailwindCSS para darle una apariencia moderna al proyecto (cosa que no era necesaria para completarlo).

Además hicimos uso de `default_model`, una clase base en Python que tiene toda la lógica del modelo (la M del patrón MVC) que después la clase `usuario` hereda para obtener un CRUD completo de manera sencilla.

La clase `default_model` se escribió en conjunto durante las clases del bootcamp, con el profesor programando. La versión inicial no usaba `dataclasses`. Propuse el cambio, el profesor lo aceptó y esa versión quedó como base genérica para el resto del curso. También la incluí en el script que generaba proyectos Flask completos con un clic, que varios compañeros usaron en los exámenes para no reescribirla por lo acotado del tiempo.

> **IMPORTANTE:** El código se publica tal como quedó en 2024, sin modificaciones posteriores.

## Stack Tecnológico
- Python.
- Pipenv.
- Flask.
- Jinja.
- MySQL.
- TailwindCSS.
 
## Requisitos
- [Python 3.13](https://www.python.org/downloads/).
- [MySQL 8](https://dev.mysql.com/downloads/) corriendo en local.
- Pipenv (se instala con `pip install pipenv`).

## ¿Cómo levantarlo?
1. Abre una terminal en una carpeta local.
2. Clona el repositorio en una carpeta local con `git clone https://github.com/Varrojalo/usuarios_crud.git` en la terminal.
3. Entra a la carpeta del proyecto con `cd usuarios_crud`.
4. Crea la BD y los datos de prueba usando `mysql -u root -p < flask_app/bd/db_usuarios.sql`.
5. Copia `.env.example` como `.env` y reemplaza los valores que dicen *"cambia-esta-clave"* por tu clave de MySQL y una clave de Flask generada.
6. Instala las dependencias `pipenv install`.
7. Levanta el servidor `pipenv run python server.py`.
8. Abre http://127.0.0.1:5000 en el navegador.

> **NOTA:** el script del paso 4 ejecuta `DROP TABLE IF EXISTS usuarios`. Si ya tienes una base llamada `esquema_usuarios`, perderás esa tabla.
