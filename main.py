"""
programa donde se utiliza las funciones basicas como ingresar,buscar,actualizar,borrar,indexar,contar,etc a un registro en una BD mongo utilizando la libreria pymongo"
"""
from pymongo import MongoClient
import cliente_repository
import datetime
import menu

# instancio objeto de Cliente_repository del modulo cliente_repository para que pueda  operar con la colection 'products' y le permite operar CRUD basico.
cliente = cliente_repository.Cliente_repository()

products_table = cliente.conexion['products']  # obtengo mi colleccion

print("---app de consola para realizar CRUD en MONGOATLAS (remoto)---")

while True:

    menu_opcion = menu.eleccionMenu()
    if menu_opcion == 0:
        break
    # funcion que muestra un menu que solicita y guarda su valor para realizar una accion determinada
    if menu_opcion == 1:
        # Obtener datos del usuario
        id_product = int(input("Ingrese el ID del producto: "))
        clase = input("Ingrese la clase del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        fecha_actual = datetime.datetime.now()

        # -----obviamente falta validar el ingreso de datos-------

        nuevo_registro = {
            "idproduct": id_product,
            "clase": clase,
            "nombre": nombre,
            "precio": precio,
            "date": fecha_actual
        }
        cliente.agregar_registro(nuevo_registro)

    elif menu_opcion == 2:
        # se buscara un registro segun el campo indicado (se mostrara por defecto el 1ero si son varios)
        print("\n**buscar producto**")

        clave = input(
            "Ingrese por el campo desea buscar un registro: ").lower()
        if clave == "clase" or clave == "nombre":
            valor = input("ingrese valor para la busqueda: ").lower()
        elif clave == "date":
            valorstr = input("ingrese valor para la busqueda: ").lower()
            valor = datetime.datetime.strptime(valorstr, "%Y-%m-%d %H:%M:%S")
        else:
            valor = int(input("Ingrese valor para la búsqueda: "))
        # creo el json para pasarlo como filtro
        filtro = {clave: valor}

        print(cliente.buscar_registro(filtro))

    elif menu_opcion == 3:
        # Actualizar un registro
        id = int(input(
            "Ingrese id del registro para actualizar: ").lower())

        clave = input(
            "Ingrese nombre del campo que desea actualizar: ").lower()
        if clave == "clase" or clave == "nombre":
            valor = input("ingrese nuevo valor para la busqueda: ").lower()
        elif clave == "date":
            valorstr = input("ingrese nuevo valor para la busqueda: ").lower()
            valor = datetime.datetime.strptime(valorstr, "%Y-%m-%d %H:%M:%S")
        else:
            valor = int(input("ingrese nuevo valor para la busqueda: "))
        json_data = {clave: valor}
        cliente.actualizar_registro(id, json_data)

    elif menu_opcion == 4:
        # Eliminar un registro
        id = int(input(
            "Ingrese id del registro para !!!ELIMINAR!!!: ").lower())
        filtro_eliminacion = {"idProduct": id}
        cliente.eliminar_registro(filtro_eliminacion)
    elif menu_opcion == 5:
        # listar todos
        for registro in cliente.obtener_todos_los_registros():
            print(registro)
    else:
        print("valor de menu incorrecto")
print("programa finalizado")
