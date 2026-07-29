import re
from functools import cached_property


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
        s = self.s
        s = s.replace("(", "_")
        s = s.replace(")", "_")
        s = s.replace("&", "_and_")
        s = s.replace("/", "_or_")
        s = s.replace(".", "_")
        s = s.replace(",", "_")
        s = s.replace(" ", "_")
        s = s.replace("-", "_")
        s = re.sub(r"_+", "_", s)
        s = s.strip('_')

        return s.lower()

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

    def shorten(self, max_len):
        if max_len < 0:
            raise ValueError("max_len must be non-negative")
        if len(self.s) <= max_len:
            return self.s
        if max_len == 0:
            return ""
        if max_len == 1:
            return self.s[0]

        s = self.s.replace("-", " ")
        words = s.split()
        if len(words) > 1:
            return "".join([word[0] for word in words[:max_len]])

        # one word case
        chars = [c for c in self.s]
        non_first_chars = chars[1:]
        consonent_non_first_chars = [
            c for c in non_first_chars if c.lower() not in "aeiou"
        ]
        return "".join([chars[0]] + consonent_non_first_chars[: max_len - 1])
