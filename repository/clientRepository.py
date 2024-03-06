from exceptions_and_validators.exception import RepositoryException
from domain.client import Client


class ClientRepository:
    def __init__(self):
        self.__client_data = {}
        self.load()

    def search(self, client_id):
        if client_id not in self.__client_data:
            raise RepositoryException("Client ID does not exist!")
        return self.__client_data[client_id]

    def add(self, client):
        if client.get_id() in self.__client_data:
            raise RepositoryException("Client ID already existing!")
        self.__client_data[client.get_id()] = client
        self.save()

    def update(self, client):
        if client.get_id() not in self.__client_data:
            raise RepositoryException("Client ID does not exist!")
        self.__client_data[client.get_id()] = client
        self.save()

    def remove(self, client_id):
        if client_id not in self.__client_data:
            raise RepositoryException("Client ID does not exist!")
        del self.__client_data[client_id]
        self.save()

    def get_all(self):
        return self.__client_data.values()

    def __len__(self):
        return len(self.__client_data)

    def load(self):
        new_data = {}
        fis = open("repository/clients.txt", "r")
        # id,nume

        line = fis.readline()
        while line != "":
            r_id, r_name = line.strip().split(',')
            r_id = int(r_id)
            r_c = Client(r_id, r_name)  # r_c = Clientul cu datele citite acum
            new_data[r_id] = r_c
            line = fis.readline()

        fis.close()
        self.__client_data = new_data

    def save(self):

        fis = open("repository/clients.txt", "w")

        for client in self.__client_data.values():
            # pentru fiecare client vedem ce trebuie salvat: id si numele
            to_write = ""
            to_write += str(client.get_id())
            to_write += "," # pentru linie noua, doar modifica separatorul in \n
            to_write += client.get_name()
            to_write += "\n"

            # salvam clientul
            fis.writelines(to_write)

        fis.close()

"""
class ClientRepositoryWithFiles(ClientRepository):

    def __init__(self):
        super(ClientRepositoryWithFiles, self).__init__()
        self.load()

    def load(self):
        new_data = {}

        fis = open("repository/clients.txt", "r")

        line = fis.readline()
        while line != "":
            r_id, r_name = line.strip().split(',')
            r_id = int(r_id)
            r_c = Client(r_id, r_name)  # r_c = Clientul cu datele citite acum
            new_data[r_id] = r_c
            line = fis.readline()

        fis.close()
        self.__client_data = new_data

    def save(self):

        fis = open("repository/clients.txt", "w")

        for client in self.__client_data.values():
            # pentru fiecare client vedem ce trebuie salvat: id si numele
            to_write = ""
            to_write += str(client.get_id())
            to_write += ","
            to_write += client.get_name()
            to_write += "\n"

            # salvam clientul
            fis.writelines(to_write)

        fis.close()
"""