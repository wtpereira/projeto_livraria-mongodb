from bson import ObjectId
from model.autor import Autor
from database.client_factory import ClientFactory

class AutorDAO:

    def __init__(self):
        self.__client: ClientFactory = ClientFactory()

    def listar(self) -> list[Autor]:
        """
        The function "listar" retrieves a list of authors from a MongoDB database and
        returns it.
        :return: a list of objects of type "Autor".
        """
        autores = list()
        client = self.__client.get_client()
        db = client.livraria
        for documento in db.autores.find():
            autor = Autor(documento.get('nome', ''), documento.get('email', ''), documento.get('telefone', ''), documento.get('bio', '--'), documento.get('_id'))
            autores.append(autor)

        client.close()
        return autores

    def adicionar(self, autor: Autor) -> None:
        """
        The function `adicionar` adds an author to a database in a bookstore.

        :param autor: The parameter "autor" is of type "Autor", which is a class
        representing an author. It has the following attributes:
        :type autor: Autor
        """
        client = self.__client.get_client()
        db = client.livraria
        db.autores.insert_one({'nome': autor.nome, 'email': autor.email, 'telefone': autor.telefone, 'bio': autor.bio})
        client.close()

    def remover(self, autor_id: str) -> bool:
        """
        The `remover` function takes an author ID as input, deletes the corresponding
        author document from a MongoDB database, and returns `True` if the deletion was
        successful, otherwise `False`.

        :param autor_id: The `autor_id` parameter is a string that represents the unique
        identifier of an author in the database
        :type autor_id: str
        :return: a boolean value. It returns True if the author with the given autor_id
        was successfully deleted from the database, and False otherwise.
        """
        client = self.__client.get_client()
        db = client.livraria
        resultado = db.autores.delete_one({'_id': ObjectId(autor_id)})
        client.close()
        if(resultado.deleted_count == 1):
            return True

        return False

    def buscar_por_id(self, autor_id: str) -> Autor:
        """
        The function `buscar_por_id` searches for an author in a database based on their
        ID and returns an `Autor` object if found.

        :param autor_id: The `autor_id` parameter is a string that represents the unique
        identifier of an author in the database
        :type autor_id: str
        :return: an instance of the `Autor` class.
        """
        autor = None
        client = self.__client.get_client()
        db = client.livraria
        documento = db.autores.find_one({'_id': ObjectId(autor_id)})
        if documento:
            autor = Autor(documento.get('nome', ''), documento.get('email', ''), documento.get('telefone', ''), documento.get('bio', '--'), documento.get('_id'))

        client.close()
        return autor

