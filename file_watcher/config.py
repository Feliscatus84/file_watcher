class WatcherConfig:
    def __init__(self, directory, interval):
        self._interval = interval
        self._directory = directory

    def interval(self) -> float:
        return self._interval

    def directory(self) -> str:
        return self._directory
