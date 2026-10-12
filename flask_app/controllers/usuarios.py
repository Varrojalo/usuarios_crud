from flask_app import app
from flask_app.models.usuario import usuario
from flask import render_template, redirect, request


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def vista_usuarios():
    lista_usuarios = usuario.all()
    return render_template('lista_usuarios.html',lista_usuarios=lista_usuarios)

@app.route('/nuevo')
def vista_nuevo():
    return render_template('nuevo.html')

@app.route('/usuarios/<int:id>')
def vista_usuario(id:int):
    data_usuario = usuario.find_by_id(id)
    return render_template('usuario.html', data=data_usuario)

@app.route('/usuarios/editar/<int:id>')
def vista_editar(id:int):
    data_usuario = usuario.find_by_id(id)
    return render_template('editar.html', data=data_usuario)



@app.route('/crear_nuevo', methods=['POST'])
def crear_usuario():

    nombre= request.form.get('INNombre'),
    apellido= request.form.get('INApellido'),
    email= request.form.get('INEmail'),

    datos = {
       "nombre": nombre,
       "apellido": apellido,
       "email": email
    }

    usuario.save(datos)
    return redirect("/usuarios")

@app.route('/editar_usuario', methods=['POST'])
def editar_usuario():
    id= request.form.get('INID'),
    nombre= request.form.get('INNombre'),
    apellido= request.form.get('INApellido'),
    email= request.form.get('INEmail'),

    datos = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "email": email
    }

    usuario.update(datos)
    return redirect("/usuarios")

@app.route('/usuarios/borrar/<int:id>', methods=['POST'])
def borrar_usuario(id: int):
    usuario.delete_by_id(id)
    return redirect("/usuarios")