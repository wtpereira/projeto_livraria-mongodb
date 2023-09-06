from bson import ObjectId
class Editora:

    def __init__(self, nome: str, endereco: str, telefone: str, id: ObjectId = None):
        """
        This is the initialization function for a editora object, which takes in various
        attributes such as name, email, phone number, biography, and an optional ID.

        :param nome: The `nome` parameter is a string that represents the name of the
        object being initialized
        :type nome: str
        :param endereco: The `endereco` parameter is a string that represents the
        address of an object
        :type endereco: str
        :param telefone: The "telefone" parameter is a string that represents the phone
        number of an object
        :type telefone: str
        :param id: The `id` parameter is an optional parameter of type `ObjectId`. It is
        used to uniquely identify an instance of the class. If no value is provided for
        `id`, it will default to `None`
        :type id: ObjectId
        """
        self.__id: ObjectId = id
        self.__nome: str = nome
        self.__endereco: str = endereco
        self.__telefone: str = telefone

    @property
    def id(self) -> ObjectId:
        return self.__id

    @id.setter
    def id(self, id: ObjectId):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
