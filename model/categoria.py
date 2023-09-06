from bson import ObjectId

class Categoria:

    def __init__(self, nome: str, id: ObjectId = None):
        """
        This is the initialization function for a categoria object, which takes in various
        attributes such as name, and an optional ID.

        :param nome: The `nome` parameter is a string that represents the name of an
        object
        :type nome: str
        :param id: The `id` parameter is an optional parameter of type `ObjectId`. It is
        used to store the unique identifier of an object. If no value is provided for
        `id`, it will default to `None`
        :type id: ObjectId
        """
        self.__id: ObjectId = id
        self.__nome: str = nome

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

    @staticmethod
    def depositar():
        return "Opa"