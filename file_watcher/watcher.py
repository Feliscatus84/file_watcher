import glob
import os
from time import sleep
from typing import List

from file_watcher.config import WatcherConfig
from file_watcher.file_list import FileSaver
from file_watcher.handler import FileHandler


class Watcher:
    def __init__(self, handlers: List[FileHandler], list_saver: FileSaver):
        self._handlers = handlers
        self._list_saver = list_saver

    def execute(self, config: WatcherConfig):
        files = self._list_saver.get_file_list()
        while True:
            current_files = []
            for file in glob.glob(config.directory(), recursive=True):
                if os.path.isfile(file):
                    current_files.append(file)
                    if file not in files:
                        print(f'New file: {file}')
                        files.append(file)
                        for handler in self._handlers:
                            if handler.is_applicable(file):
                                handler.handle(file)
            for file in files:
                if file not in current_files:
                    print(f'File deleted: {file}')
                    files.remove(file)
            self._list_saver.save_file_list(files)
            sleep(config.interval())
