import os
import tempfile

import requests

from utils_future.misc.Log import Log
from utils_future.file.File import File
log = Log("WWW")


class WWW:
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f"🌐{self.url}"

    def download(self, output_file=None):
        
        if output_file.exists():
            return

        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        content = response.text

        File(output_file.path).write(content)
        log.debug(f"Downloaded {self} to {output_file}")
        