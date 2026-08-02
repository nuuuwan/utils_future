import os
import shutil
import tempfile

from utils_future.file.FileOrDirectory import FileOrDirectory


class Directory(FileOrDirectory):
    def make(self):
        os.makedirs(self.path, exist_ok=True)

    def remove(self):
        if self.exists():
            shutil.rmtree(self.path)

    @classmethod
    def get_temp(cls, *args):
        directory = cls(tempfile.gettempdir(), *args)
        return directory

    def __iter__(self):
        from utils_future.file.File import File

        if not self.exists():
            return
        for name in os.listdir(self.path):
            child_path = os.path.join(self.path, name)
            if os.path.isdir(child_path):
                yield Directory(child_path)
            else:
                yield File(child_path)
