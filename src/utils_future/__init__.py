# flake8: noqa: F408

from utils_future.file.Directory import Directory
from utils_future.file.File import File
from utils_future.file.JSONFile import JSONFile
from utils_future.file.PDFFile import PDFFile
from utils_future.file.TSVFile import TSVFile
from utils_future.misc.Format import Format
from utils_future.misc.Log import Log
from utils_future.misc.Markdown import Markdown
from utils_future.misc.Parse import Parse
from utils_future.misc.ShallowDict import ShallowDict
from utils_future.misc.String import String
from utils_future.misc.WWW import WWW
from utils_future.time.Time import Time
from utils_future.time.TimeFormat import TimeFormat

import os
class osx:
    @staticmethod
    def startfile(path: str):
        os.system(f"open {path}")