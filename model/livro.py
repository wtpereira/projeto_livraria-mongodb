from bson import ObjectId
from model.categoria import Categoria
from model.editora import Editora
from model.autor import Autor

class Livro:

    def __init__(self, titulo: str, resumo: str, ano: int, paginas: int, isbn: str, categoria: Categoria, editora: Editora, autor: Autor, id: ObjectId = None):
        """
        This is the initialization function for a livro object, which takes in various
        attributes such as title, summary, year, pages, ISBN, category, publisher,
        author, and an optional ID.

        :param titulo: This parameter represents the title of the book. It is of type
        str, which means it should be a string
        :type titulo: str
        :param resumo: The parameter "resumo" is a string that represents a summary or
        brief description of the book
        :type resumo: str
        :param ano: The "ano" parameter represents the year in which the book was
        published. It is of type int
        :type ano: int
        :param paginas: The parameter "paginas" represents the number of pages in a book
        :type paginas: int
        :param isbn: The ISBN (International Standard Book Number) is a unique
        identifier for books. It is a 10 or 13-digit number that helps identify a
        specific edition of a book
        :type isbn: str
        :param categoria: The parameter "categoria" is of type "Categoria". It
        represents the category of the book
        :type categoria: Categoria
        :param editora: The parameter "editora" represents the publisher of the book. It
        is of type "Editora", which is likely a class representing a publisher entity
        with its own attributes and methods
        :type editora: Editora
        :param autor: The "autor" parameter is of type "Autor", which represents the
        author of the book
        :type autor: Autor
        :param id: The `id` parameter is an optional parameter that represents the
        unique identifier of the book. It is of type `ObjectId`, which is typically used
        in MongoDB databases to uniquely identify documents. If no `id` is provided, it
        will default to `None`
        """
        self.__id: ObjectId = id
        self.__titulo: str = titulo
        self.__resumo: str = resumo
        self.__ano: int = ano
        self.__paginas: int = paginas
        self.__isbn: str = isbn
        self.__categoria: Categoria = categoria
        self.__editora: Editora = editora
        self.__autor: Autor = autor

    @property
    def id(self) -> ObjectId:
        return self.__id

    @id.setter
    def id(self, id: ObjectId):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @titulo.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        self.__categoria = categoria

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor