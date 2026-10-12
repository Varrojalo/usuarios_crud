
from dataclasses import dataclass, fields
from datetime import datetime
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL

from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class default_model:
    table_name: ClassVar[str] = None

    id: int
    created_at: datetime
    updated_at: datetime

    def __init__(self,data):
        
        for field in fields(self):
            setattr(self, field.name, data.get(field.name))

    # Método para obtener todos los registros de la tabla
    @classmethod
    def all(cls):
        query = f'SELECT * FROM {cls.table_name}'
        results = connectToMySQL(os.getenv("DB_NAME")).query_db(query)
        instances = []
        for result in results:
            instances.append(cls(result))
        return instances
    
    # Método para obtener el registros de la tabla segun el id
    @classmethod
    def find_by_id(cls, id):
        try:
            query = f"SELECT * from {cls.table_name} WHERE id={id}"
            result = connectToMySQL(os.getenv("DB_NAME")).query_db(query)
            return cls(result[0])
        except:
            return None
    @classmethod
    def save(cls, data):
        string_fields = cls.get_fields()
        string_values = cls.get_data_values()
        query = f'INSERT INTO {cls.table_name} ({string_fields}) VALUES ({string_values})'
        return connectToMySQL(os.getenv("DB_NAME")).query_db(query, data)

    @classmethod
    def replace(cls, data):
        string_fields = cls.get_fields()
        string_values = cls.get_data_values()
        query = f'REPLACE INTO {cls.table_name} ({string_fields}) VALUES ({string_values})'
        return connectToMySQL(os.getenv("DB_NAME")).query_db(query, data)

    @classmethod
    def update(cls, query, data):
        query = query
        return connectToMySQL(os.getenv("DB_NAME")).query_db(query, data)
    
    @classmethod
    def update_by_id(cls, data):
        string_fields = cls.get_fields()
        string_values = cls.get_data_values()
        query = f'UPDATE {cls.table_name} ({string_fields}) VALUES ({string_values})'
        return connectToMySQL(os.getenv("DB_NAME")).query_db(query, data)
    
    @classmethod
    def delete_by_id(cls, id:int):
        query = f"DELETE FROM {cls.table_name} WHERE id={id}"
        result = connectToMySQL(os.getenv("DB_NAME")).query_db(query)

    # Método para ver todos los campos
    @classmethod
    def data_fields(cls):
        class_data_fields = []
        for field in fields(cls):
            if (field.name != 'id' and field.name != 'created_at' and field.name != 'updated_at'):
                class_data_fields.append(field.name)
        return class_data_fields

    @classmethod
    def get_fields(cls):
        return ', '.join(cls.data_fields())

    @classmethod
    def get_data_values(cls):
        return ', '.join([f'%({field})s' for field in cls.data_fields()])