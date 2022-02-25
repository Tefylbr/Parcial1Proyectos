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


SQL = "SELECT * FROM Parcial1_4;"
INSERT = "INSERT INTO PArcial1_4(Numero, Tipo) VALUES (%s, %s);"

while ciclo == 1:

    print("Seleccione una opcion")
    print("Comenzar...................................(c)")
    print("Ver historial de base de datos.............(h)")
    print("Salir......................................(o)")
    

    Opcion = str(input())
    try: 
        if Opcion == "c": 
            x = int(input("Ingrese un numero para verificar si es primo o compuesto: "))
            valor = range(2,x)
            contador = 0
            for n in valor:               
                if x % n == 0: 
                    contador += 1
                    print("Divisor: ", n)

            if contador > 0:
                print("El numero es compuesto")
                tipo = "Compuesto"
            else: 
                print("EL numero es primo")
                tipo = "Primo"
            try:
                cursor = conexion.cursor()                    
                cursor.execute (INSERT, (x, tipo))
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
        if not type(x, tipo) is int:
            raise TypeError("Solo numeros aceptados")
            
    if Opcion == "o":
                ciclo=0
                print("Sthephanie Lorena Bonilla Rodriguez 201900300")
                cursor.close()
                conexion.close()