#!/usr/bin/env python3
"""
Anglerfish - Two LEDs for a wearable deep-sea prop.

Hardware:
    Lure (yellow):   220ohm resistor -> GPIO 18 (Pin 12), GND (Pin 6)
    Stomach (red):   220ohm resistor -> GPIO 13 (Pin 33), GND (Pin 34)
"""

from gpiozero import PWMLED
from signal import pause


def main():
    lure = PWMLED(18)     # Yellow LED - the glowing lure
    stomach = PWMLED(13)  # Red LED - the stomach glow

    # Lure: slow hypnotic pulse (2.5s in, 2.5s out = 5s cycle)
    lure.pulse(fade_in_time=2.5, fade_out_time=2.5)

    # Stomach: slower breathing (3.7s in, 3.7s out = 7.4s cycle)
    # Non-divisible cycle lengths so they constantly drift out of sync
    stomach.pulse(fade_in_time=3.7, fade_out_time=3.7)

    try:
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        lure.close()
        stomach.close()


if __name__ == "__main__":
    main()
