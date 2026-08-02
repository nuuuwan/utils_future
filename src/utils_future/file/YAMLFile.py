import yaml

from utils_future.file.File import File


class YAMLFile(File):
    ENCODING = "utf-8"

    def read(self):
        with open(self.path, "r", encoding=self.ENCODING) as f:
            return yaml.safe_load(f)

    def write(self, content):
        with open(self.path, "w", encoding=self.ENCODING) as f:
            yaml.safe_dump(content, f, allow_unicode=True, sort_keys=False)

    def write_lines(self, lines):
        content = "\n".join(lines)
        with open(self.path, "w", encoding=self.ENCODING) as f:
            f.write(content)
