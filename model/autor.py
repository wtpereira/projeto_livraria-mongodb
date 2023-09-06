from bson import ObjectId

class Autor:

    def __init__(self, nome: str, email: str, telefone: str, bio: str, id: ObjectId = None):
        """
        This is the initialization function for a autor object, which takes in various
        attributes such as name, email, phone number, biography, and an optional ID.

        :param nome: A string representing the name of the person
        :type nome: str
        :param email: The email parameter is a string that represents the email address
        of a person
        :type email: str
        :param telefone: The `telefone` parameter is a string that represents the phone
        number of a person
        :type telefone: str
        :param bio: A string that represents the biography or description of the person
        :type bio: str
        :param id: The `id` parameter is an optional parameter of type `ObjectId`. It is
        used to uniquely identify an instance of the class. If no value is provided for
        `id`, it will default to `None`
        :type id: ObjectId
        """
        self.__id: ObjectId = id
        self.__nome: str = nome
        self.__email: str = email
        self.__telefone: str = telefone
        self.__bio: str = bio

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
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def bio(self) -> str:
        return self.__bio

    @bio.setter
    def bio(self, bio: str):
        self.__bio = bio