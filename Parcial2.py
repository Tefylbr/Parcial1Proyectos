import psycopg2 
import statistics 
import numpy as np

ciclo = 1
mayor = 0
menor = 100

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


SQL = "SELECT * FROM Parcial1_2;"
INSERT = "INSERT INTO PArcial1_2(nota1, nota2, nota3, nota4, nota5, media, mediana, moda, rango, desviacion, varianza) VALUES (%s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s);"

while ciclo == 1:

    print("Seleccione una opcion")
    print("Comenzar...................................(c)")
    print("Ver historial de base de datos.............(h)")
    print("Salir......................................(o)")
    

    Opcion = str(input())
    try: 
        if Opcion == "c": 
            
            print("Ingrese a continuacion sus calificaciones")
            a =  float(input("Ingrese la primera calificación: "))
            b =  float(input("Ingrese la segunda calificación: "))
            c =  float(input("Ingrese la tercera calificación: "))
            d =  float(input("Ingrese la cuarta calificación: "))
            e =  float(input("Ingrese la quinta calificación: "))
            notas = [a,b,c,d,e]
            media = statistics.mean(notas)
            mediana = statistics.median(notas)
            moda = statistics.mode(notas)
            desviacion = statistics.pstdev(notas)
            varianza = statistics.variance(notas)
            for i in range(len(notas)):
                num = notas[i]
                if num > mayor:
                    mayor = num
            for i in range(len(notas)):
                num = notas[i]
                if num < menor:
                    menor = num
            rango = mayor - menor 
            print("Las notas son: ", a, ", ",b, ", " ,c, ", ",d, ", ",e)
            print("La media es: ", media)
            print("La mediana es: ", mediana)
            print("La moda es: ", moda)
            print("La desviacion es: ", desviacion)
            print("La varianza es: ", varianza)
            print("El rango es: ", rango)
            try:
                cursor = conexion.cursor()                    
                cursor.execute (INSERT, (a,b,c,d,e,media,mediana,moda,rango,desviacion,varianza))
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
        if not type(a,b,c,d,e) is float:
            raise TypeError("Solo numeros aceptados")
            
    if Opcion == "o":
                ciclo=0
                print("Sthephanie Lorena Bonilla Rodriguez 201900300")
                cursor.close()
                conexion.close()
        

