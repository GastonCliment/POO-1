"""
class Persona {
  - nombre
  - apellido
  + Persona(nombre: str, apellido: str): Persona
  + fullName(): string
  + iniciales(): string
}
"""


class Persona:
    def __init__(self, nombre: str, apellido: str):
        self._nombre = nombre
        self._apellido = apellido

    def full_name(self) -> str:
        usuario: str = self._nombre + self._apellido
        return usuario

    def iniciales(self) -> str:
        iniciales = self._nombre[:2] + "." + self._apellido[:2]
        return iniciales


if __name__ == '__main__':
    usuario = Persona("Gaston ", "Climent")
    print(usuario.full_name())
    print(usuario.iniciales())
