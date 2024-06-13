import sqlite3

def getData(table):

    tableLower = table.lower()

    try:
        conn = sqlite3.connect("./dbconection/ma.db")
        cursor = conn.cursor()
        #instruction = f"SELECT * FROM insumos;"
        instruction = f"SELECT * FROM {tableLower};"
        cursor.execute(instruction)
        response = cursor.fetchall()
        conn.commit()
        conn.close()
        return response
    
    except TypeError as e:
        print(e)


def getForValue(table, atribute, val):
    tableLower = table.lower()
    atributeLower = atribute.lower()
    valUp = val.upper()

    try:
        conn = sqlite3.connect("./dbconection/ma.db")
        cursor = conn.cursor()
        #instruction = f"SELECT * FROM insumos;"
        instruction = f"SELECT * FROM {tableLower} WHERE {atributeLower} LIKE '%{valUp}%';"
        cursor.execute(instruction)
        response = cursor.fetchall()
        conn.commit()
        conn.close()
        return response
    
    except TypeError as e:
        print(e)


def getToIdClient(id):
    conn = sqlite3.connect("./dbconection/ma.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM clientes WHERE id_registro LIKE '{id}'"
    cursor.execute(instruction)
    response = cursor.fetchall()
    conn.commit()
    conn.close()

    return response

def getToIdSupply(id):
    conn = sqlite3.connect("./dbconection/ma.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM insumos WHERE id_insumo LIKE '{id}'"
    cursor.execute(instruction)
    response = cursor.fetchall()
    conn.commit()
    conn.close()

    return response

def getSupplies():
    conn = sqlite3.connect("./dbconection/ma.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM insumos;"
    cursor.execute(instruction)
    response = cursor.fetchall()
    conn.commit()
    conn.close()

    return response