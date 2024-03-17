import signal
import sys

import board
import gpiozero

from hsv import Hsv
from led import Led


class Footlight:
    def __init__(
        self,
        led_pin: str,
        power_button_pin: str,
        hue_button_pin: str,
        saturation_up_button_pin: str,
        saturation_down_button_pin: str,
        value_up_button_pin: str,
        value_down_button_pin: str,
    ) -> None:
        self._led = Led(
            pin=getattr(board, f"D{led_pin}"),
            number=3,
            value_step=0.005,
        )
        self._led.color_set(Hsv(1.0, 1.0, 0.005))
        self._power_button = gpiozero.Button(power_button_pin)
        self._hue_button = gpiozero.Button(hue_button_pin)
        self._saturation_up_button = gpiozero.Button(saturation_up_button_pin)
        self._saturation_down_button = gpiozero.Button(
            saturation_down_button_pin
        )
        self._value_up_button = gpiozero.Button(value_up_button_pin)
        self._value_down_button = gpiozero.Button(value_down_button_pin)

        self._setup_callback()

    def _setup_callback(self) -> None:
        self._power_button.when_activated = self._led.power_toggle
        self._hue_button.when_activated = self._led.hue_change_cw
        self._saturation_up_button.when_activated = self._led.saturation_up
        self._saturation_down_button.when_activated = self._led.saturation_down
        self._value_up_button.when_activated = self._led.value_up
        self._value_down_button.when_activated = self._led.value_down

        signal.signal(signal.SIGTERM, lambda signum, frame: self.close())

    def close(self) -> None:
        self._led.close()
        sys.exit(0)

    def loop(self) -> None:
        signal.pause()
