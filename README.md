# Aplicación de Consola para CRUD en MongoDB

Este programa de consola permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MongoDB remota utilizando la biblioteca pymongo.

## Requisitos

- Python 3.x
- pymongo

## Instalación

1. Instala Python desde [python.org](https://www.python.org/downloads/)
2. Instala la biblioteca pymongo ejecutando el siguiente comando:
"pip install pymongo"


## Configuración

- Asegúrate de tener una base de datos MongoDB en línea a la que puedas acceder.
- Actualiza la cadena de conexión en el archivo `cliente_repository.py` con tus propias credenciales de MongoDB.
- para obtener tus creedenciales: ve a mongoAtlas y en el apartadado Database Deployments
![Database Deployments](https://i.ibb.co/Z6qsyF9/mongo-inactivo.png)
dale click en Connect,deberias visualizar algo asi...
![Connect](https://i.ibb.co/G070m6Y/pasos-para-obtener-direccion.jpg)
## Uso

Ejecuta el archivo principal `main.py` y sigue las instrucciones del menú para realizar operaciones CRUD en la base de datos MongoDB.

```bash
python main.py
```
Deberia ver una imagen como esta:
![MENU](https://i.ibb.co/9w070Lt/menu.jpg)


## Funcionalidades:

- Agregar Registro: Ingresa datos para crear un nuevo registro en la base de datos.

- Buscar Registro: Busca un registro según un campo específico.

- Actualizar Registro: Actualiza un registro existente según su ID.

- Eliminar Registro: Elimina un registro según su ID.

- Listar Todos: Muestra todos los registros en la base de datos.
