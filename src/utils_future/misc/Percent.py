from functools import cached_property


class Percent:
    def __init__(self, _value: float):
        self._value = _value

    @cached_property
    def humanize(self) -> str:
        if self._value < 0:
            return "-" + Percent(-self._value).humanize

        if self._value < 0.01:
            return "<0.01%"

        return f"{self._value:.0%}"
    