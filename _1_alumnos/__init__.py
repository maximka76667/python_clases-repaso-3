from Alumno import Alumno
from Administrator import Administrator

administrator = Administrator()

# Anadir alumnos
administrator.anhadir_alumno(Alumno("H2", "Pablo", "Avda 1", "12345"))
administrator.anhadir_alumno(Alumno("H2", "Marcos", "Avda 2", "7689"))  # Ya existe alumno con dni H2

# Mostrar datos de alumno si existe
administrator.mostrar_alumno("H3")  # Alumno no existe

# Mostrar datos de todos alumnos
administrator.ver_alumnos()
