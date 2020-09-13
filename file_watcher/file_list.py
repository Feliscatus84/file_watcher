import abc
import pickle
from typing import List


class FileSaver(abc.ABC):

    @abc.abstractmethod
    def save_file_list(self, file_list):
        pass

    @abc.abstractmethod
    def get_file_list(self) -> List:
        pass


class SimpleTextFileSaver(FileSaver):
    def __init__(self, path):
        self._path = path

    def save_file_list(self, file_list):
        with open(self._path, 'w') as file_list_writer:
            for file in file_list:
                file_list_writer.write(f'{file}\n')

    def get_file_list(self) -> List:
        files = []
        with open(self._path) as file_list_reader:
            for file in file_list_reader:
                files.append(file.strip())
        return files


class PickleFileSaver(FileSaver):
    def __init__(self, path):
        self._path = path

    def save_file_list(self, file_list):
        with open(self._path, 'bw') as file_list_writer:
            pickle.dump(file_list, file_list_writer)

    def get_file_list(self) -> List:
        with open(self._path, 'br') as file_list_reader:
            return pickle.load(file_list_reader)