import csv
from functools import cache

from utils_future.file.File import File
from utils_future.misc.Log import Log

log = Log("TSVFile")


class TSVFile(File):
    @cache
    def read(self):
        with open(self.path, encoding="utf-8") as f:
            reader = csv.reader(f, delimiter="\t")
            headers = next(reader)
            d_list = [dict(zip(headers, row)) for row in reader if row]
            return d_list


    def write(self, d_list):
        if not d_list:
            raise ValueError("Cannot write an empty list to TSV file.")
        first_d = d_list[0]
        if not isinstance(first_d, dict):
            raise ValueError("Each item in the list must be a dictionary.")

        headers = list(first_d.keys())
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter="\t")
            writer.writeheader()
            writer.writerows(d_list)
            