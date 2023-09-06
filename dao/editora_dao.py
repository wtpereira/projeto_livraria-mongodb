from bson import ObjectId
from model.editora import Editora
from database.client_factory import ClientFactory

class EditoraDAO:

    def __init__(self):
        self.__client: ClientFactory = ClientFactory()

    def listar(self) -> list[Editora]:
        """
        The function "listar" retrieves a list of "Editora" objects from a MongoDB
        database.
        :return: The method `listar` returns a list of `Editora` objects.
        """
        editoras = list()
        client = self.__client.get_client()
        db = client.livraria
        for documento in db.editoras.find():
            editora = Editora(documento['nome'], documento['endereco'], documento['telefone'], documento['_id'])
            editoras.append(editora)

        client.close()
        return editoras

    def adicionar(self, editora: Editora) -> None:
        """
        The function `adicionar` adds a new document to the "editoras" collection in a
        MongoDB database.

        :param editora: The parameter `editora` is of type `Editora`, which is an object
        representing an editora (publisher) in a bookstore. It contains the following
        attributes:
        :type editora: Editora
        """
        client = self.__client.get_client()
        db = client.livraria
        db.editoras.insert_one({'nome': editora.nome, 'endereco': editora.endereco, 'telefone': editora.telefone})
        client.close()

    def remover(self, editora_id: str) -> bool:
        """
        The `remover` function deletes an editora (publisher) from a MongoDB database
        based on its ID and returns a boolean indicating whether the deletion was
        successful.

        :param editora_id: The `editora_id` parameter is a string that represents the
        unique identifier of the editora (publisher) that you want to remove from the
        database
        :type editora_id: str
        :return: a boolean value. It returns True if the deletion of the editora
        document with the given editora_id was successful (deleted_count is 1), and
        False otherwise.
        """
        client = self.__client.get_client()
        db = client.livraria
        resultado = db.editoras.delete_one({'_id': ObjectId(editora_id)})
        client.close()
        if resultado.deleted_count == 1:
            return True

        return False

    def buscar_por_id(self, editora_id: str) -> Editora:
        """
        The function `buscar_por_id` searches for an editora (publisher) in a MongoDB
        database based on its ID and returns an instance of the Editora class if found.

        :param editora_id: The `editora_id` parameter is a string that represents the
        unique identifier of an editora (publisher) in the database
        :type editora_id: str
        :return: an instance of the class `Editora` if a document with the specified
        `editora_id` is found in the database. If no document is found, it returns
        `None`.
        """
        editora = None
        client = self.__client.get_client()
        db = client.livraria
        documento = db.editoras.find_one({'_id': ObjectId(editora_id)})
        if documento:
            editora = Editora(documento['nome'], documento['endereco'], documento['telefone'], documento['_id'])

        client.close()
        return editora
