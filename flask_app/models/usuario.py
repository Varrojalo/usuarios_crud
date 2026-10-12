from dataclasses import dataclass
from typing import ClassVar

from flask_app.models.default_model import default_model


# Creamos la clase basada en la tabla de mascotas
@dataclass(init=False)
class usuario(default_model):
    table_name: ClassVar[str] = 'usuarios'

    # Atributos de la clase
    nombre: str
    apellido : str
    email: str

    @classmethod
    def update(cls, data):
        tabla = cls.table_name
        query = 'UPDATE usuarios SET nombre=%(nombre)s,apellido=%(apellido)s,email=%(email)s WHERE id=%(id)s'
        super().update(query,data)

if __name__ == '__main__':

    lista_usuarios = usuario.all()
    print(lista_usuarios)
    print("------")
    print(usuario.find_by_id(1))


