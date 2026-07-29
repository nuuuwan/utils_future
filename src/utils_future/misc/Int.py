import math
from functools import cached_property


class Int:
    def __init__(self, _value):
        self._value = _value

    @cached_property
    def humanize(self) -> str:
        if self._value < 0:
            return "-" + Int(-self._value).humanize

        if self._value < 1000:
            return str(self._value)

        for log_1000, label in [
            [1, 'K'],
            [2, 'M'],
            [3, 'B'],
            [4, 'T'],
            [5, 'P'],
            [6, 'E'],
        ]:
            threshold = 1000 ** (log_1000 + 1)
            if self._value < threshold:
                mask = 1000.0**log_1000
                display_value = self._value / mask
                decimal_places_in_value = math.floor(
                    math.log10(display_value)
                )
                decimal_places_to_display = max(
                    0, 1 - decimal_places_in_value
                )
                ndigits = 1 - decimal_places_in_value
                rounded_value = round(display_value, ndigits)
                return f"{rounded_value:.{decimal_places_to_display}f}{label}"

        raise ValueError(f"Value {self._value} is too large to humanize")
