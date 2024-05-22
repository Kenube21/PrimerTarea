from os import system
import time
import Enlace as conn
db = conn.DB()

def registrar_movimiento(accion,detalle):
    sql= "INSERT INTO movimientos (accion,detalle) VALUES (?,?)"
    parametros= (accion,detalle)
    db.ejecutar_consulta(sql,parametros)

def add():
    codigo= int(input("Ingrese Codigo de Producto por favor: "))
    nombre= str(input("Ingrese Nombre de Producto por favor: "))
    precio= int(input("Ingrese Precio de Producto por favor: "))
    cantidad= int(input("Ingrese Cantidad de Producto por favor: "))
    bodega= int(input("Ingrese Bodega donde esta el Producto por favor: "))
    pasillo= int(input("Ingrese Pasillo donde esta el Producto por favor: "))
    estante= int(input("Ingrese Estante donde esta el Producto por favor: "))
    if(codigo!=0 and len(nombre)>0 and precio!=0 and cantidad!=0 and bodega!=0 and pasillo!=0 and estante!=0):
        sql= "INSERT INTO productos (codigo,nombre,precio,cantidad,bodega,pasillo,estante) VALUES (?,?,?,?,?,?,?)"
        parametros= (codigo,nombre,precio,cantidad,bodega,pasillo,estante)
        db.ejecutar_consulta(sql,parametros)
        print("Registrado con exito")
        registrar_movimiento("producto",f"Se añadio {nombre}")
    else:
        print("Valor No Ingresado")
def subtract():
    codigo= int(input("Ingrese Codigo de Producto por favor: "))
    cantidad_restar=int(input("Ingrese Cantidad a Retirar por favor: "))
    if(codigo!=0 and cantidad_restar!=0):
        sql_consultar = "SELECT cantidad FROM productos WHERE codigo=?"
        cantidad_actual = db.consultar_por_id(sql_consultar,(codigo,))
        if(cantidad_actual[0] >= cantidad_restar):
            sql= "UPDATE productos SET cantidad=cantidad-? WHERE codigo=?"
            parametros = (cantidad_restar,codigo)
            db.ejecutar_consulta(sql,parametros)
            print("Se retiro con exito")
            registrar_movimiento("retiro",f"Se retiró {cantidad_restar} unidades del producto {codigo}")
        else:
            print("La cantidad a retirar en mayor a la existente")
    else:
        print("Digite datos Validos")
def enter():
    codigo= int(input("Ingrese Codigo de Producto por favor: "))
    cantidad_suma=int(input("Ingrese Cantidad a Ingresar por favor: "))
    if(codigo!=0 and cantidad_suma!=0):
            sql= "UPDATE productos SET cantidad=cantidad+? WHERE codigo=?"
            parametros= (cantidad_suma,codigo)
            db.ejecutar_consulta(sql,parametros)
            print("Se Añadio con exito")
            registrar_movimiento("adicion",f"Se añadio {cantidad_suma} unidades del producto {codigo}")
    else:
        print("Digite datos Validos")
def search():
    sql= "SELECT * FROM productos"
    result= db.ejecutar_consulta(sql)
    for data in result:
        print("""
        Codigo:   {}
        Nombre:   {}
        Precio:   {}
        Cantidad: {}
        Bodega:   {}
        Pasillo:  {}
        Estante:  {}
        """. format (data[0],data[1],data[2],data[3],data[4],data[5],data[6],))
    registrar_movimiento("consulta",f"se consultaron todos los productos")
def specify():
    codigo= int(input("Ingrese Codigo de Producto por favor: "))
    if (codigo!=0):
        sql="SELECT * FROM productos WHERE codigo like ?"
        parametros = ('%{}%'.format(codigo),)
        result = db.ejecutar_consulta(sql, parametros)
        for data in result:
            print("""
            Codigo:   {}
            Nombre:   {}
            Precio:   {}
            Cantidad: {}
            Bodega:   {}
            Pasillo:  {}
            Estante:  {}
            """. format (data[0],data[1],data[2],data[3],data[4],data[5],data[6],))
        registrar_movimiento("consulta_especifica",f"Se consulto el codigo {codigo}")
def movements():
    sql= "SELECT * FROM movimientos"
    result= db.ejecutar_consulta(sql)
    for data in result:
        print("""
        Accion:    {}
        Detalle:   {}
        """. format (data[1],data[2],))


while True:
    print("*********************************")
    print("       \tProyecto_Kendall        ") 
    print("*********************************")
    print("\t[1] Ingresar Producto.")
    print("\t[2] Retiro de Productos.")
    print("\t[3] Añadir a Productos.")
    print("\t[4] Cosulta de Productos.")
    print("\t[5] Consulta de Producto Especifico.")
    print("\t[6] Consultar Movimientos")
    print("\t[7] Salir del sistema.")
    print("*********************************")
    try:
            opcion = int (input("Seleccione una Opcion: "))
            if (opcion == 1):
                add()
                time.sleep(1)
                system("clear")
            elif(opcion == 2):
                subtract()
                time.sleep(1)
                system("clear")
            elif(opcion == 3):
                enter()
                time.sleep(1)
                system("clear")
            elif(opcion == 4):
                search()
                time.sleep(1)
                system("clear")
            elif(opcion == 5):
                specify()
                time.sleep(1)
                system("clear")
            elif(opcion == 6):
                movements()
                time.sleep(1)
                system("clear")
            elif(opcion == 7):
                break
            else:
                print("Opcion no Valida")
    except ValueError:
        print("El tipo de dato es Incorrecto")       
    except Exception as error:
        #print(error)
        print("Seleccione una opcion correcta")
        system("clear")
