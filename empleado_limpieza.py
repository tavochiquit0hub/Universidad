# empleado_limpieza.py
from empresa import Empresa
from persona import Persona

class EmpleadoLimpieza(Persona, Empresa):
    def __init__(self):
        Persona.__init__(self)
        Empresa.__init__(self)
        self._numero_empleado = ""
        self._turno = ""

    # Getter y Setter
    def get_numero_empleado(self):
        return self._numero_empleado

    def set_numero_empleado(self, numero_empleado):
        self._numero_empleado = numero_empleado

    def get_turno(self):
        return self._turno

    def set_turno(self, turno):
        self._turno = turno

    def mostrar_informacion(self):
        persona_info = Persona.mostrar_informacion(self)
        empresa_info = Empresa.mostrar_informacion_empresa(self)
        return f"{persona_info}, Número de Empleado: {self._numero_empleado}, {empresa_info}, Turno: {self._turno}"
