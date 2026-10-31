from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Biblioteca
'''

@dataclass()
class Biblioteca:
    id: int
    nome: str
    indirizzo: str

    def __eq__(self, other):
        return isinstance(other, Biblioteca) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"
