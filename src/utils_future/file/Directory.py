import os
import tempfile

from utils_future.file.FileOrDirectory import FileOrDirectory


class Directory(FileOrDirectory):
    def make(self):
        os.makedirs(self.path, exist_ok=True)

    @classmethod
    def get_temp(cls, *args):
        directory = cls(tempfile.gettempdir(), *args)
        directory.make()
        return directory

    def __iter__(self):
        if not self.exists():
            return iter([])
        return iter(os.listdir(self.path))
