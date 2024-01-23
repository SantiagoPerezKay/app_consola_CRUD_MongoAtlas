import datetime
from pymongo import MongoClient


class Cliente_repository:
    conexion = None

    def __init__(self):
        self.conexion = self.obtener_conexion()

    def obtener_conexion(self):
        try:
            if self.conexion is None:
                return MongoClient("mongodb+srv://admin:admin@cluster0.dm9lnki.mongodb.net/?retryWrites=true&w=majority").test
            return None
        except:
            return None


# agregar registro

    def agregar_registro(self, data):
        try:
            result = self.conexion.products.insert_one(data)
            print(f"Registro agregado con el ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error al agregar registro: {e}")

    def buscar_registro(self, filtro):
        try:
            result = self.conexion.products.find_one(filtro)
            if result:
                print("Registro encontrado:")
                print(result)
            else:
                print("Registro no encontrado.")
        except Exception as e:
            print(f"Error al buscar registro: {e}")

    def actualizar_registro(self, id_product, update_data):
        try:
            filtro = {"idProduct": id_product}
            actualizacion = {"$set": update_data}

            resultado = self.conexion.products.update_one(
                filtro, actualizacion)

            if resultado.matched_count > 0:
                print("Registro actualizado exitosamente.")
            else:
                print("Registro no encontrado.")
        except Exception as e:
            print(f"Error al actualizar registro: {e}")

    def eliminar_registro(self, filtro):
        try:
            result = self.conexion.products.delete_one(filtro)
            print(f"{result.deleted_count} registro(s) eliminado(s).")
        except Exception as e:
            print(f"Error al eliminar registro: {e}")

    def obtener_todos_los_registros(self):
        try:
            lista = self.conexion.products.find({})
            return list(lista)
        except Exception as e:
            print(f"Error al obtener todos los registros: {e}")
            return []
