import psycopg2 
ciclo = 1
try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "1234",
        dbname = "ejemploconnpy"
    )
    print("conexion exitosa")
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("Verifique los parametros")


SQL = "SELECT * FROM Parcial1_3;"
INSERT = "INSERT INTO PArcial1_3(Monto,SinIva, ConIva) VALUES (%s, %s,%s);"

while ciclo == 1:

    print("Seleccione una opcion")
    print("Comenzar...................................(c)")
    print("Ver historial de base de datos.............(h)")
    print("Salir......................................(o)")
    

    Opcion = str(input())
    try: 
        if Opcion == "c": 
            monto = int(input("Ingrese un monto en quetzales: "))
            x = monto * 0.12 
            y = monto + x
            print("El monto sin IVA es: ", monto)
            print("El monto con IVA es: ",  y)
            try:
                cursor = conexion.cursor()                    
                cursor.execute (INSERT, (monto, monto, y))
                conexion.commit()
            except: 
                print("Datos ingresados incorrectos")

        elif Opcion == "h":
                cursor = conexion.cursor()
                cursor.execute(SQL)
                valores = cursor.fetchall()
                cursor.close()
                conexion.close()
                print(valores)
        if Opcion != "o": 
            print("Pulse cualquier tecla para regresar al menu")
            Opcion = str(input())
    except: 
        if not type(monto, y) is int:
            raise TypeError("Solo numeros aceptados")
            
    if Opcion == "o":
                ciclo=0
                print("Sthephanie Lorena Bonilla Rodriguez 201900300")
                cursor.close()
                conexion.close()