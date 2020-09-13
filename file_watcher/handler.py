import abc
import shutil


class FileHandler(abc.ABC):
    @abc.abstractmethod
    def is_applicable(self, file) -> bool:
        pass

    @abc.abstractmethod
    def handle(self, file):
        pass


class FileLogHandler(FileHandler):
    def handle(self, file):
        pass

    def is_applicable(self, file) -> bool:
        return True


class AnyFileHandler(FileHandler):
    def __init__(self, path_map):
        self._path_map = path_map

    def is_applicable(self, file) -> bool:
        if file.split('.')[-1] in self._path_map.keys():
            return True
        return False

    def handle(self, file):
        shutil.copy(file, self._path_map[file.split('.')[-1]])
