import os

from utils_future.file.Directory import Directory
from utils_future.file.FileOrDirectory import FileOrDirectory


class File(FileOrDirectory):
    ENCODING = "utf-8"

    def read(self):
        with open(self.path, "r", encoding=self.ENCODING) as f:
            return f.read()

    def write(self, data):
        with open(self.path, "w", encoding=self.ENCODING) as f:
            return f.write(data)

    def delete(self):
        if self.exists():
            os.remove(self.path)

    def get_parent_directory(self):
        parent_path = os.path.dirname(self.path)
        return Directory(parent_path)
