clc;
clear;
pkg load database
c= true;
while c
  try
    fprintf("\n Elija una opcion \n 1.Comenzar \n 2.Mostrar Historial \n");
    n=(input('  '));
    if n>2||n==0|n<0
      fprintf("Elija una opcion correcta \n");
    endif
    if n==1
      n1=input('Ingrese un numero para saber si es primo o ocmpuesto:\n');
      valor = range(2,x)
      contador = 0
      for n in valor:               
          if x Mod n == 0: 
             contador += 1
             fprintf('Divisor: ', n);
             
          if contador > 0:
                fprintf('El numero es compuesto');
                tipo = 'Compuesto'
          else: 
              fprintf('EL numero es primo');
              tipo = 'Primo'
    endif
    
      params= cell(1,5);
      params{1,1}=x;
      params{1,2}=x;
      params{1,2}=tipo;
      
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','1234'));
      N=pq_exec_params(conn, "insert into Parcial1_4(Numero, Tipo) VALUES (%s, %s);",(n1,n1,Total); %insertar datos en la tabla
      c=false;
   
    if n==2
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','1234'));
      N=pq_exec_params(conn, "Select * from Parcial1_4;"); %insertar datos en la tabla
      disp(N)
      c=false;
    endif
  catch
    fprintf("Valor incorrecto, ingreselo de nuevo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile