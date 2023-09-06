from bson import ObjectId
from model.categoria import Categoria
from database.client_factory import ClientFactory


class CategoriaDAO:

    def __init__(self):
        self.__client: ClientFactory = ClientFactory()

    def listar(self) -> list[Categoria]:
        """
        The `listar` function retrieves a list of `Categoria` objects from a MongoDB
        database.
        :return: The method `listar` is returning a list of `Categoria` objects.
        """
        categorias = list()
        client = self.__client.get_client()
        db = client.livraria
        for documento in db.categorias.find():
            cat = Categoria(documento['nome'], documento['_id'])
            categorias.append(cat)

        client.close()
        return categorias

    def adicionar(self, categoria: Categoria) -> None:
        """
        The function `adicionar` adds a new category to a MongoDB database.

        :param categoria: The parameter "categoria" is of type "Categoria"
        :type categoria: Categoria
        """
        client = self.__client.get_client()
        db = client.livraria
        db.categorias.insert_one({'nome': categoria.nome})
        client.close()

    def remover(self, categoria_id: str) -> bool:
        """
        The `remover` function deletes a category from a MongoDB database based on its
        ID and returns `True` if the deletion was successful, otherwise it returns
        `False`.

        :param categoria_id: The `categoria_id` parameter is a string that represents
        the unique identifier of a category in the database
        :type categoria_id: str
        :return: a boolean value. It returns True if a document with the given
        categoria_id is successfully deleted from the database, and False otherwise.
        """
        client = self.__client.get_client()
        db = client.livraria
        resultado = db.categorias.delete_one({'_id': ObjectId(categoria_id)})
        client.close()
        if resultado.deleted_count == 1:
            return True

        return False

    def buscar_por_id(self, categoria_id: str) -> Categoria:
        """
        The function `buscar_por_id` searches for a category by its ID in a MongoDB
        database and returns a `Categoria` object if found.

        :param categoria_id: The `categoria_id` parameter is a string that represents
        the ID of the category you want to search for
        :type categoria_id: str
        :return: an instance of the `Categoria` class.
        """
        cat = None
        client = self.__client.get_client()
        db = client.livraria
        documento = db.categorias.find_one({'_id': ObjectId(categoria_id)})
        if documento:
            cat = Categoria(documento['nome'], documento['_id'])

        client.close()
        return cat
