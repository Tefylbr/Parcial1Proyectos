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


SQL = "SELECT * FROM Parcial1_1;"
INSERT = "INSERT INTO PArcial1_1(num1,num2,resultado) VALUES (%s, %s,%s);"

while ciclo == 1:

    print("Seleccione una opcion")
    print("Comenzar...................................(c)")
    print("Ver historial de base de datos.............(h)")
    print("Salir......................................(o)")
    

    Opcion = str(input())
    try: 
        if Opcion == "c": 
            x =  int(input("Lanze el dado e ingrese el numero que obtuvo: "))  
            y =  int(input("Lanze nuevamente el dado e ingrese el nuevo numero: "))
            z = x + y 
            print("Resultado de la suma es:", z)
            if z == 8  :
                print("Ha ganado")
                r = "ganado"
                try:
                    cursor = conexion.cursor()                    
                    cursor.execute (INSERT, (x, y, r))
                    conexion.commit()
                except: 
                    print("Datos ingresados incorrectos")
            elif z == 7:
                print("Ha perdido")
                r = "perdido"
                try:
                    cursor = conexion.cursor()                    
                    cursor.execute (INSERT, (x, y, r))
                    conexion.commit()
                except: 
                    print("Datos ingresados incorrectos")
            else:
                print("Intentelo de nuevo")
                while z != 7 and z!= 8:
                    x =  int(input("Lanze el dado e ingrese el numero que obtuvo: "))  
                    y =  int(input("Lanze nuevamente el dado e ingrese el nuevo numero: "))
                    z = x + y 
                    if z == 8 :
                        print("Ha ganado")
                        r = "ganado"
                        try:
                            cursor = conexion.cursor()                    
                            cursor.execute (INSERT, (x, y, r))
                            conexion.commit()
                        except: 
                            print("Datos ingresados incorrectos")
                    elif z == 7:
                        print("Ha perdido")
                        r = "perdido"
                        try:
                            cursor = conexion.cursor()                    
                            cursor.execute (INSERT, (x, y, r))
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
        if not type(x, y) is int:
            raise TypeError("Solo numeros aceptados")
            
    if Opcion == "o":
                ciclo=0
                print("Sthephanie Lorena Bonilla Rodriguez 201900300")
                cursor.close()
                conexion.close()
        










#Juego simulado del Gran 8
#La Reglas del juego. Debes lanzar un par de dados. Si la suma de las caras es un 8, ganas. Si sale 7, pierdes. Si no ha
#salido, ni 8, ni 7, puedes seguir lanzando. Si sale 8 ganas, pero si en algún otro lanzamiento sale 7, pierdes.