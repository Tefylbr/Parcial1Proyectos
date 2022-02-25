clc;
clear;
pkg load database
retry= true;
while retry
  try
    fprintf("\n Elija una opcion \n 1.Comenzar \n 2.Mostrar Historial \n");
    n=(input('Elija:   '));
    if n>2||n==0|n<0
      fprintf("Elija una opcion correcta \n");
    endif
    if n==1
      n1=input("Nota 1:\n");
      n2=input("Nota 2:\n");
      n3=input("Nota 3:\n");
      n4=input("Nota 4:\n");
      n5=input("Nota 5:\n");
      notas = [n1,n2,n3,n4,n5]
      media=(n1+n2+n3+n4+n5)/5;
      mediana = median(notas);
      moda= mode(notas);
      desviacion= std(x);
      varianza = var(x);     
        
       print("Las notas son: ", n1, ", ",n2, ", " ,n3, ", ",n4, ", ",n4);
       print("La media es: ", media);
       print("La mediana es: ", mediana);
       print("La moda es: ", moda);
       print("La desviacion es: ", desviacion);
       print("La varianza es: ", varianza);
       print("El rango es: ", rango);
          
    endif
    
      params= cell(1,5);
      params{1,1}=n1;
      params{1,2}=n2;
      params{1,3}=n3;
      params{1,4}=n4;
      params{1,5}=n5;
      params{1,6}=media;
      params{1,7}=mediana;
      params{1,8}=moda;
      params{1,9}=rango;
      params{1,10}=desviacion;
      params{1,11}=varianza;
      
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','123fgthg'));
      N=pq_exec_params(conn, "insert into Parcial1_2(nota1, nota2, nota3, nota4, nota5, media, mediana, moda, rango, desviacion, varianza) VALUES (%s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s);",params); %insertar datos en la tabla
      c=false;
   
    if n==2
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','1234'));
      N=pq_exec_params(conn, "Select * from Parcial1_2;"); %insertar datos en la tabla
      disp(N)
      retry=false;
    endif
  catch
    fprintf("Valor incorrecto, ingreselo de nuevo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile