import os

from footlight import Footlight


def run() -> None:
    footlight = Footlight(
        led_pin=os.environ["FOOTLIGHT_LED_PIN"],
        power_button_pin=os.environ["FOOTLIGHT_POWER_BUTTON_PIN"],
        hue_button_pin=os.environ["FOOTLIGHT_HUE_BUTTON_PIN"],
        saturation_up_button_pin=os.environ[
            "FOOTLIGHT_SATURATION_UP_BUTTON_PIN"
        ],
        saturation_down_button_pin=os.environ[
            "FOOTLIGHT_SATURATION_DOWN_BUTTON_PIN"
        ],
        value_up_button_pin=os.environ["FOOTLIGHT_VALUE_UP_BUTTON_PIN"],
        value_down_button_pin=os.environ["FOOTLIGHT_VALUE_DOWN_BUTTON_PIN"],
    )
    footlight.loop()


if __name__ == "__main__":
    run()
