import pickle

from file_watcher.file_list import SimpleTextFileSaver, PickleFileSaver
from file_watcher.handler import FileLogHandler, AnyFileHandler
from file_watcher.watcher import Watcher
from file_watcher.config import WatcherConfig

paths = {'txt': './target_folder/texts', 'mp4': './target_folder/movies', 'jpg': './target_folder/images',
                'jpeg': './target_folder/images', 'png': './target_folder/images', 'gif': './target_folder/images'}

supported_handlers = [
    # FileLogHandler(),
    AnyFileHandler(paths)
]

watcher = Watcher(supported_handlers, PickleFileSaver('pickled_file_list.json'))
watcher.execute(WatcherConfig('./example_folder/**', 10.0))


# paths z zewnętrznego pliku
# file list dla danego folderu
# testy
