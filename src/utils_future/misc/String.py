import re
from functools import cache, cached_property, lru_cache
import json
_SNAKE_TABLE = str.maketrans(
    {
        "(": "_",
        "*": "",
        ")": "_",
        "&": "_and_",
        "/": "_or_",
        ".": "_",
        ",": "_",
        " ": "_",
        "-": "_",
    }
)
_MULTI_UNDERSCORE = re.compile(r"_+")  # compiled once, module level


@lru_cache(maxsize=None)
def _to_snake(s: str) -> str:
    s = s.translate(_SNAKE_TABLE)
    s = _MULTI_UNDERSCORE.sub("_", s)
    return s.strip("_").lower()


class String:
    def __init__(self, s: str):
        self.s = s

    @cached_property
    def cleaned_s(self) -> str:
        return self.s.strip().replace(",", "").replace(" ", "_").lower()

    @cached_property
    def pascal(self) -> str:
        s = self.s
        s = s.replace("&", "_and_")
        s = s.replace("/", "_or_")
        s = s.replace(".", "_")
        s = s.replace(",", "_")
        s = s.replace(" ", "_")
        s = s.replace("-", "_")
        s = "".join(c if c.isalnum() else "_" for c in s)

        return "".join(word.capitalize() for word in s.split("_"))

    @cached_property
    def snake(self) -> str:
        return _to_snake(self.s)

    @cached_property
    def int(self) -> int:
        try:
            return int(float(self.cleaned_s))
        except ValueError:
            return None

    @cached_property
    def float(self) -> float:
        try:
            return float(self.cleaned_s)
        except ValueError:
            return None

    @staticmethod
    def join(*s_list: list[str]):
        return " ".join(s_list)

    @cache
    def shorten(self, max_len):
        if max_len < 0:
            raise ValueError("max_len must be non-negative")
        if len(self.s) <= max_len:
            return self.s
        if max_len == 0:
            return ""
        if max_len == 1:
            return self.s[0]

        if max_len > 3:
            max_len = 3

        s = self.s.replace("-", " ")
        words = s.split()
        if len(words) > 1:
            return "".join([word[0] for word in words]).upper()

        # one word case
        chars = [c for c in self.s]
        non_first_chars = chars[1:]
        consonent_non_first_chars = [
            c for c in non_first_chars if c.lower() not in "aeiou"
        ]
        return "".join(
            [chars[0]] + consonent_non_first_chars[: max_len - 1]
        ).upper()


    @cached_property 
    def json(self) -> str:    
        return json.dumps(self.s, ensure_ascii=False, indent=4)