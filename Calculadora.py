"""Ejercicio: Compañia rappy solicita un sistema que determine los dias vacacionales de un trabajador. Tomando en cuenta
las siguientes caracteristicas:
Atención al cliente (clave 1):
-Reciben 6 días vacacionales por 1 año de servicio.
-14 días vacacionales por 2 a 6 años de serv.
-20 días vacacionales a partir de 7 años de serv.

Logistica (clave 2):
-Reciben 7 días vacacionales por 1 año de servicio.
-15 días vacacionales por 2 a 6 años de serv.
-22 días vacacionales a partir de 7 años de serv.

Gerencia (clave 3):
-Reciben 10 días vacacionales por 1 año de servicio.
-20 días vacacionales por 2 a 6 años de serv.
-30 días vacacionales a partir de 7 años de serv.

Requerimientos:
El sistema debe solicitar: Nombre, Clave de departamento y Antiguedad del trabajador desde teclado.
El programa debe mostrar un mensaje en pantalla que contenga el nombre del L y los días de vacaciones que tienen derecho.
"""
print("SISTEMA DE CONTROL VACACIONAL RAPPY")
print("===================================")

nombre_empleado = input("Por favor introduce el nombre del empleado: ")
clave_departamento = int(input("Introduce por favor la clave del departamento: "))
antiguedad_empleado = float(input("Por introduce los años laborados del empleado: "))

if clave_departamento == 1:
    
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 6 días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 14 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 días de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, "aun no tiene derecho a vacaciones.")


    
elif clave_departamento == 2:
    
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 7 días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 15 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 22 días de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, "aun no tiene derecho a vacaciones.")


elif clave_departamento == 3:
    
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, "tiene derecho a 10 días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 30 días de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, "aun no tiene derecho a vacaciones.")


else:
    print("La clave del departametno no existe, vuelve a intentarlo.")

    
