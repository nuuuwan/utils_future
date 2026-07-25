import os
import tempfile

import requests

from utils_future.misc.Log import Log

log = Log("WWW")


class WWW:
    def __init__(self, url: str):
        self.url = url

    def __str__(self):
        return f"🌐{self.url}"

    def download(self, output_file=None):
        if output_file is None:
            suffix = os.path.splitext(self.url)[-1] or '.tmp'
            _, path = tempfile.mkstemp(suffix=suffix)
            response = requests.get(self.url, timeout=30)
            response.raise_for_status()
            with open(path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            log.debug(f"Downloaded {self} to {path}")
            return path

        if output_file.exists():
            return

        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        content = response.text

        output_file.write(content)
        log.debug(f"Downloaded {self} to {output_file}")
