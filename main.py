# main.py
from estudiantes import Estudiantes
from profesores import Profesores
from administrativos import Administrativos
from empleado_limpieza import EmpleadoLimpieza

def main():
    # Crear objetos
    estudiante = Estudiantes()
    estudiante.get_nombre()
    #estudiante.set_nombre('Juan')
    estudiante.set_apellido("Pérez")
    estudiante.set_edad(20)
    estudiante.set_matricula("123456")
    estudiante.set_carrera("Ing en Sistemas")
    estudiante.set_semestre("Segundo")

    profesor = Profesores()
    profesor.set_nombre("María")
    profesor.set_apellido("López")
    profesor.set_edad(40)
    profesor.set_departamento("Matemáticas")
    profesor.set_categoria("Tiempo Completo")
    profesor.set_maximmo_grado_de_estudio("Maestria")

    administrativo = Administrativos()
    administrativo.set_nombre("Carlos")
    administrativo.set_apellido("González")
    administrativo.set_edad(35)
    administrativo.set_cargo("Secretario")
    administrativo.set_area("Academia")

    empleado_limpieza = EmpleadoLimpieza()
    empleado_limpieza.set_nombre("Pedro")
    empleado_limpieza.set_apellido("Martínez")
    empleado_limpieza.set_edad(45)
    empleado_limpieza.set_numero_empleado("E1234")
    empleado_limpieza.set_nombre_empresa("Limpieza S.A.")
    empleado_limpieza.set_direccion("Calle Ficticia 123")
    empleado_limpieza.set_turno("Tarde")

    # Mostrar información
    print("Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nProfesor:")
    print(profesor.mostrar_informacion())

    print("\nAdministrativo:")
    print(administrativo.mostrar_informacion())

    print("\nEmpleado de Limpieza:")
    print(empleado_limpieza.mostrar_informacion())

if __name__ == "__main__":
    main()
