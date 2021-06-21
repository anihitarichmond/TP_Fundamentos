#3 USO DE BASE DE DATOS

# import sqlite3
# import pandas as pd
# import datetime
#
#
# conexion = sqlite3.connect("CLIENTES.db")
# cursor = conexion.cursor()


# sentenciaSQL = "CREATE TABLE clientes"
# sentenciaSQL = sentenciaSQL + "(nro INTEGER NOT NULL,"
# sentenciaSQL = sentenciaSQL + "nombre VARCHAR(100) NOT NULL,"
# sentenciaSQL = sentenciaSQL + "apellido VARCHAR(100) NOT NULL,"
# sentenciaSQL = sentenciaSQL + "telefono INTEGER NOT NULL,"
# sentenciaSQL = sentenciaSQL + "fecha TIMESTAMP NOT NULL,"
# sentenciaSQL = sentenciaSQL + "fecha_entrega INTERGER NOT NULL,"
# sentenciaSQL = sentenciaSQL + "orden TEXT NOT NULL,"
# sentenciaSQL = sentenciaSQL + "total INTEGER NOT NULL)"
#
# sentenciaSQL2 = "CREATE TABLE Materia_Prima"
# sentenciaSQL2 = sentenciaSQL2 + "(nombre VARCHAR(100) NOT NULL,"
# sentenciaSQL2 = sentenciaSQL2 + "stock INTEGER NOT NULL)"


# nro = int(input('ingrese el nro:'))
# nombre = str(input('ingrese el nombre:'))
# apellido = str(input('ingrese el apellido:'))
# telefono = int(input('ingrese el nro de telefono:'))
# fecha = datetime.datetime.now()
#fecha_entrega = datetime.datetime.strptime(input('ingrese fecha y hora de entrega: '))

# def comprobar_fecha(text):
#     try:
#         datetime.datetime.strptime(text, '%Y/%m/%d')
#     except:
#         return "El formato debe ser  YYYY/MM/DD"
#     return datetime.datetime.strptime(text, '%Y/%m/%d')
#
# fecha_entrega = input("ingrese la fecha de entrega: ")
#
# comprobar_fecha(fecha_entrega)
#
# sabor = str(input('¿vainilla, chocolate o brownie? '))
# relleno = str(input('¿ddl, crema y frutillas o nutella? '))
# tipo = str(input('¿letter o number cake? '))
# tamanio = str(input('¿pequenia, mediana o grande? '))
# decoracion = str(input('¿flores comestibles, cobertura de chocolate o nada? '))
# orden = '{}; {}; {}; {}; {}'.format(sabor,relleno,tipo,tamanio, decoracion)
# precio = int(input('ingrese el precio: $'))
#
#
# clientes = [
#             (nro, nombre, apellido, telefono, fecha, fecha_entrega, orden, precio)
#         ]
# sentenciaSQL = "INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?, ?)"


# Materia_Prima = [
#     ('Harina', 2000),
#     ('Chocolate', 5000),
#     ('Dulce de Leche', 5500),
#     ('Huevos', 3000),
#     ('Frutillas', 6600),
#     ('Crema', 2000),
#     ('Nutella', 5500),
#     ('Esencia de Vainilla', 1500)
# ]
# sentenciaSQL2 = "INSERT INTO Materia_Prima VALUES (?, ?)"
#
#
# cursor.execute(sentenciaSQL)
# cursor.execute(sentenciaSQL2)
# cursor.executemany(sentenciaSQL, clientes)
# cursor.executemany(sentenciaSQL2, Materia_Prima)
# conexion.commit()
# conexion.close()
# '''
# FUNCION str2
# si algun caracter es un nro lanzo except
#
# '''
# Pandas me permite trabajar con estructuras amigables (csv, pkl, db)
#
# Conexion --> hago la conexion con la db. Acá se me crea el db de covid y se me agrega a carpeta en la compu.
#
# El cursor me permite ejecutar: llamar a una db, crear tablas, etc.
#
# CREATE TABLE --> creo las tablas y les agrego los campos que quiero que tenga
#                 INTEGER: para números enteros
#                 TEXT: sólo texto
#                 TIMESTAMP: devuelve una indicación de fecha y hora a partir de un valor o par de valores.
#                 NOT NULL:   obliga a que un campo siempre contenga un valor, lo que significa que no puede insertar un
#                             nuevo registro o actualizar un registro sin agregar un valor a este campo.
#                 VARCHAR (100): almacena series de caracteres, los datos pueden consistir en letras, números y símbolos.
#
# Input -->   para poder ingresar datos desde la terminal.
#             int: los input son siempre datos de tipo stream, es por eso que a los datos numéricos le pongo int delante
#                 para transformarlos.
#
# {} . format(variables) -->  para poder ingresar varios datos de varias variables a la terminal a partir de un solo campo
#                             en el db.
#
# INSERT INTO ... VALUES (?) -->  una vez creada la tabla, quiero ingresarle datos. Por eso primero creo una variable
#                                 definiendo lo que quiero agregar, luego le ingreso la cantidad de ? necesarios
#                                 dependiendo la cantidad de campos que tiene mi tabla.
#
# Executemany --> le indico la funcion de ejecutar varias entradas de valores dentro de una misma tabla.
#
# Commit -->  define el final de una transacción ejecutada con éxito. Este comando asegura que todas las modificaciones
#             efectuadas durante la transacción se vuelvan parte permanente de la base.
#

#4. LECTURA DE TEXTO PLANO: BLOCK DE NOTAS

from io import open
archivo = open('Naposbakery.txt', 'r+')
lista = archivo.readlines()
lista[3] = '- Chocolate\n- Vainilla\n- Brownie'
lista[8] = '- Dulce de leche\n- Crema y frutillas\n- Nutella'
lista[13] = '- Letter Cake\n- Number Cake'
lista[17] = '- Pequenio\n- Mediano\n- Grande'
lista[22] = '- Flores Comestibles\n- Cobertura de Chocolate'
archivo.seek(0)
archivo.writelines(lista)

archivo.close()
del (archivo)
with open('Naposbakery.txt', 'r+') as archivo:
    print(archivo.read())


# r+ -->  Cuando queremos abrir un archivo en modo lectura,pero a su vez querramos tener la posibilidad de sobreescribir
#         parte del mismo.
#
# archivo.seek(0) --> Cuando indicamos a partir de qué parte quiero que inicie el puntero y desde ahí contar el índice
#                     para modificar las notas.
#
# del (archivo) -->   Es optativa, aunque nos asegura liberar de la memoria los recursos que utilizó Python para operar
#                     sobre el archivo.
#                     En programas cortos esta línea no es absolutamente necesaria, sin embargo, en sistemas de gran
#                     envergadura es una buena práctica ir liberando la memoria que ya no vamos a utilizar.



