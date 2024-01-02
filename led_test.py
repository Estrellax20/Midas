from lib.neopixel import Neopixel
from config import *

strip = Neopixel(1, 0, LED_PIN, "GRB")
strip.brightness(LED_BRIGHTNESS)
strip.fill(LED_COLORS['blue'])
strip.show()
