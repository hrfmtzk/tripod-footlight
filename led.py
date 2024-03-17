import types
import typing

import neopixel

from hsv import Hsv

if typing.TYPE_CHECKING:
    import microcontroller


class Led:
    def __init__(
        self,
        pin: "microcontroller.Pin",
        number: int,
        hue_step_dgree: float = 10.0,
        saturation_step: float = 0.05,
        value_step: float = 0.05,
    ) -> None:
        self._powered = False
        self._hsv = self._get_default_hsv()
        self._pixels = neopixel.NeoPixel(pin=pin, n=number)
        self._hue_step_dgree = hue_step_dgree
        self._saturation_step = saturation_step
        self._value_step = value_step

        self.off()

    def _get_default_hsv(self) -> Hsv:
        return Hsv(0.0, 0.0, 1.0)  # white

    def _flush(self) -> None:
        if self._powered:
            self._pixels.fill(self._hsv.get_rgb255())
        else:
            self._pixels.fill(0)

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type: typing.Optional[typing.Type[BaseException]],
        exception_value: typing.Optional[BaseException],
        traceback: typing.Optional[types.TracebackType],
    ):
        self.close()

    def close(self) -> None:
        self.off()
        self._pixels.deinit()

    def off(self) -> None:
        self._powered = False
        self._flush()

    def on(self) -> None:
        self._powered = True
        self._flush()

    def power_toggle(self) -> None:
        if self._powered:
            self.off()
        else:
            self.on()

    def color_set(self, hsv: Hsv) -> None:
        self._hsv = hsv
        self._flush()

    def color_reset(self) -> None:
        self._hsv = self._get_default_hsv()
        self._flush()

    def hue_change_cw(self, step: int = 1) -> None:
        self._hsv.add_hue_dgree(self._hue_step_dgree * step)
        self._flush()

    def hue_change_ccw(self, step: int = 1) -> None:
        self._hsv.add_hue_dgree(-self._hue_step_dgree * step)
        self._flush()

    def saturation_up(self, step: int = 1) -> None:
        self._hsv.add_saturation(self._saturation_step * step)
        self._flush()

    def saturation_down(self, step: int = 1) -> None:
        self._hsv.add_saturation(-self._saturation_step * step)
        self._flush()

    def value_up(self, step: int = 1) -> None:
        self._hsv.add_value(self._value_step * step)
        self._flush()

    def value_down(self, step: int = 1) -> None:
        self._hsv.add_value(-self._value_step * step)
        self._flush()
