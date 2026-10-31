from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Libro
'''

@dataclass()
class Libro:
    id: int
    titolo: str
    autore: str
    genere: str
    anno_pubblicazione: int
    id_biblioteca: int

    def __eq__(self, other):
        return isinstance(other, Libro) and self.id == other.id

    def __str__(self):
        return (f"{self.id} | {self.titolo} | Autore: {self.autore} | Genere: {self.genere} | "
                f"Anno: {self.anno_pubblicazione} | Biblioteca: {self.id_biblioteca}")

    def __repr__(self):
        return (f"{self.id} | {self.titolo} | Autore: {self.autore} | Genere: {self.genere} | "
                f"Anno: {self.anno_pubblicazione} | Biblioteca: {self.id_biblioteca}")
