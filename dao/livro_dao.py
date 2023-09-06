from bson import ObjectId

from model.livro import Livro
from database.client_factory import ClientFactory
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.autor_dao import AutorDAO


class LivroDAO:

    def __init__(self):
        self.__client: ClientFactory = ClientFactory()

    def listar(self) -> list[Livro]:
        """
        The `listar` function retrieves a list of books from a MongoDB database and
        returns them as a list of `Livro` objects.
        :return: The method `listar` returns a list of `Livro` objects.
        """
        livros = list()
        client = self.__client.get_client()
        db = client.livraria
        for documento in db.livros.find():
            categoria = CategoriaDAO().buscar_por_id(documento['categoria_id'])
            editora = EditoraDAO().buscar_por_id(documento['editora_id'])
            autor = AutorDAO().buscar_por_id(documento['autor_id'])
            livro = Livro(documento['titulo'],
                        documento.get('resumo', ''),
                        documento['ano'],
                        documento['paginas'],
                        documento['isbn'],
                        categoria,
                        editora,
                        autor,
                        documento['_id'])
            livros.append(livro)

        client.close()
        return livros

    def adicionar(self, livro: Livro) -> None:
        """
        The function `adicionar` adds a book to a MongoDB database.

        :param livro: The parameter "livro" is of type "Livro", which is a class
        representing a book. It contains the following attributes:
        :type livro: Livro
        """
        client = self.__client.get_client()
        db = client.livraria
        db.livros.insert_one({
            'titulo': livro.titulo,
            'resumo': livro.resumo,
            'ano': livro.ano,
            'paginas': livro.paginas,
            'isbn': livro.isbn,
            'categoria_id': str(livro.categoria),
            'editora_id': str(livro.editora),
            'autor_id': str(livro.autor.id)
        })
        client.close()

    def remover(self, livro_id: str) -> bool:
        """
        The `remover` function takes a book ID as input, deletes the corresponding book
        from a MongoDB database, and returns `True` if the deletion was successful,
        otherwise `False`.

        :param livro_id: The `livro_id` parameter is a string that represents the unique
        identifier of a book in the database
        :type livro_id: str
        :return: a boolean value. It returns True if a document with the given livro_id
        is successfully deleted from the database, and False otherwise.
        """
        client = self.__client.get_client()
        db = client.livraria
        resultado = db.livros.delete_one({'_id': ObjectId(livro_id)})
        client.close()
        if resultado.deleted_count == 1:
            return True

        return False

    def buscar_por_id(self, livro_id: str) -> Livro:
        """
        The function `buscar_por_id` searches for a book in a MongoDB database by its ID
        and returns a `Livro` object if found.

        :param livro_id: The `livro_id` parameter is a string that represents the unique
        identifier of a book
        :type livro_id: str
        :return: a Livro object.
        """
        livro = None
        client = self.__client.get_client()
        db = client.livraria
        documento = db.livros.find_one({'_id': ObjectId(livro_id)})
        if documento:
            livro = Livro(documento['nome'], documento['_id'])

        client.close()
        return livro
