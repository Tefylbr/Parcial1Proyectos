clc; clear all; close all;
pkg load database;
c= true;
c2= true;

while c
  try
    fprintf("\n Elija una opcion");
    fprintf("\n 1.Comenzar \n 2.Comenzar \n 3.Salir\n")
    n=(input(' '));
    if n>3||n==0|n<0
      fprintf("Elija una opcion correcta \n");
    endif
    if n==1
      while c2
        try
          
          a = input(fprintf("Lance el dado el ingrese el valor obtenido: %d \n"));
          b= input(fprintf("Lance el dado nuevamente e ingrese el valor: %d \n"));
          r=a+b;
          if r==8
            tipo="Has ganado";
            fprintf("%r \n", status);
            fprintf("\n");
            conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
            'port','5432','user','postgres','password','1234'));
            N=pq_exec_params(conn, "insert into Parcial1_1(num1, num2, resultado) values($1,$2,$3);", (a, b, tipo));  
            c2=false;
          endif
          if r==7
            tipo="Has perdido";
            fprintf("%s \n", status);
            conn = pq_connect(setdbopts('dbname','ejemploconnpy ','host','localhost',
            'port','5432','user','postgres','password','1234'));
            N=pq_exec_params(conn, "insert into Parcial1_1(num1, num2, resultado) values($1,$2,$3);",(a,b,tipo)); 
          else
            status="Intentelo de nuevo";
            fprintf("%s \n", status);
            conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
            'port','5432','user','postgres','password','1234'));
            N=pq_exec_params(conn, "insert into dados(num1,num2,resultado) values($1,$2,$3);",(a,b,tipo)); %i

        catch
          fprintf("Valor incorrecto, ingreselo de nuevo %d \n");
          msg = lasterror.message;
          fprintf(msg);
        end_try_catch
      endwhile

    endif
    if n==2
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','1234'));
      N=pq_exec_params(conn, "Select * from angle;"); %insertar datos en la tabla
      disp(N)
      c=false;
    endif
    
    ifn==3
      c=false;
    endif
  catch
    fprintf("A ingresado un valor erroneo vuelva a intentarlo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile