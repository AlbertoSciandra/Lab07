from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def get_generi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro"
        cursor.execute(query)
        for row in cursor:
            if row["genere"]:
                result.append(row["genere"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_libri_filtrati(biblioteca, genere):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor(dictionary=True)

        # Query con COALESCE per gestire i filtri opzionali come spiegato nel lab
        query = """
                SELECT DISTINCT l.* FROM libro l
                JOIN copia c ON l.id = c.id_libro
                JOIN biblioteca b ON c.id_biblioteca = b.id
                WHERE b.nome = COALESCE(%s, b.nome)
                  AND l.genere = COALESCE(%s, l.genere)
            """
        cursor.execute(query, (biblioteca, genere))
        for row in cursor:
            result.append(row)

        cursor.close()
        cnx.close()
        return result