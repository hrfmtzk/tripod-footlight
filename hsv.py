import colorsys
import typing


class Hsv:
    def __init__(self, hue: float, saturation: float, value: float) -> None:
        self._hue = hue
        self._saturation = saturation
        self._value = value
        self._normalize()

    def __clip_0_to_1(self, value: float) -> float:
        return min(max(value, 0.0), 1.0)

    def _normalize(self) -> None:
        self._hue = self._hue % 360.0
        self._saturation = self.__clip_0_to_1(self._saturation)
        self._value = self.__clip_0_to_1(self._value)

    def add_hue_dgree(self, dgree: float) -> None:
        self._hue += dgree
        self._normalize()

    def add_saturation(self, value: float) -> None:
        self._saturation += value
        self._normalize()

    def add_value(self, value: float) -> None:
        self._value += value
        self._normalize()

    def get_rgb255(self) -> tuple[int, int, int]:
        return typing.cast(
            tuple[int, int, int],
            tuple(
                map(
                    lambda c: int(c * 255),
                    colorsys.hsv_to_rgb(
                        self._hue / 360.0,
                        self._saturation,
                        self._value,
                    ),
                )
            ),
        )
