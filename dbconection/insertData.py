import sqlite3
from src.components.MBox import MBox

def insertNewClient(val1, val2, val3, val4, val5, val6):

    try:
        conn=sqlite3.connect("./dbconection/ma.db")
        cursor = conn.cursor()
        instruction = f"INSERT INTO clientes (patente, marca, modelo, nombre, fecha, descripcion) VALUES ('{val1}','{val2}', '{val3}', '{val4}', '{val5}', '{val6}');"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
        MBox("success", "nuevo service guardado con éxito.")
    except TypeError as e:
        print(e)

def insertNewSupply(val1, val2, val3, val4, val5, val6):

    try:
        conn=sqlite3.connect("./dbconection/ma.db")
        cursor = conn.cursor()
        instruction = f"INSERT INTO insumos (insumo_nombre, costo_unidad, precio_venta, ganancia, dinero_invertido, stock) VALUES ('{val1}','{val2}', '{val3}', '{val4}', '{val5}', '{val6}');"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
        MBox("success", "nuevo insumo guardado con éxito.")
    except TypeError as e:
        print(e)