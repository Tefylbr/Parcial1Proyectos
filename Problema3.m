clc;
clear;
pkg load database
c= true;
while c
  try
    fprintf("\n Elija una opcion \n 1.Comenzar \n 2.Mostrar Historial \n");
    n=(input(' '));
    if n>2||n==0|n<0
      fprintf("Elija una opcion correcta \n");
    endif
    if n==1
      n1=input("Ingrese el monto en qurtzales para calcualr el IVA:\n");
      Iva= n1*0.12
      Total = n1+Iva
      fprintf("El monto sin IVA es : Q", n1);
      fprintf("El monto con IVA es: Q", Total);      
    endif
    
      params= cell(1,5);
      params{1,1}=n1;
      params{1,2}=Total;

      
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','1234'));
      N=pq_exec_params(conn, "insert into Parcial1_3(Monto, SinIva, ConIva) VALUES (%s, %s,%s);",(n1,n1,Total); %insertar datos en la tabla
      c=false;
   
    if n==2
      conn = pq_connect(setdbopts('dbname','ejemploconnpy','host','localhost',
      'port','5432','user','postgres','password','1234'));
      N=pq_exec_params(conn, "Select * from Parcial1_3;"); %insertar datos en la tabla
      disp(N)
      c=false;
    endif
  catch
    fprintf("Valor incorrecto, ingreselo de nuevo %d \n");
    msg = lasterror.message;
    fprintf(msg);
  end_try_catch
endwhile