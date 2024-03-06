from exceptions_and_validators.exception import RepositoryException
from domain.movie import Movie


class MovieRepository:
    def __init__(self):
        self.__movie_data = dict()
        self.load()


    def search(self, movie_id):
        if movie_id not in self.__movie_data:
            raise RepositoryException("Movie ID does not exist!")
        return self.__movie_data[movie_id]

    def add(self, movie):
        if movie.get_id() in self.__movie_data:
            raise RepositoryException("Movie ID already existing!")
        self.__movie_data[movie.get_id()] = movie
        self.save()

    def update(self, movie):
        if movie.get_id() not in self.__movie_data:
            raise RepositoryException("Movie ID does not exist!")
        self.__movie_data[movie.get_id()] = movie
        self.save()

    def remove(self, movie_id):
        if movie_id not in self.__movie_data:
            raise RepositoryException("Movie ID does not exist!")
        del self.__movie_data[movie_id]
        self.save()

    def get_all(self):
        return self.__movie_data.values()

    def __len__(self):
        return len(self.__movie_data)

    def load(self):

        new_data = {}

        fis = open("repository/films.txt", "r")
        # id,nume

        line = fis.readline()
        while line != "":
            r_id = line.strip()
            r_id = int(r_id)
            line = fis.readline().strip()
            r_title = line.strip()
            line = fis.readline().strip()
            r_gen = line.strip()
            line = fis.readline().strip()
            r_description = line.strip()
            r_c = Movie(r_id, r_title,r_gen,r_description)
            new_data[r_id] = r_c
            line = fis.readline()

        fis.close()

        self.__movie_data = new_data

    def save(self):

        fis = open("repository/films.txt", "w")

        for movie in self.__movie_data.values():
            to_write = ""
            to_write += str(movie.get_id())
            to_write += "\n"
            to_write += movie.get_title()
            to_write += "\n"
            to_write += movie.get_genre()
            to_write += "\n"
            to_write += movie.get_description()
            to_write += "\n"

            fis.writelines(to_write)

        fis.close()
