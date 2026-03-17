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

    # Lure: slow hypnotic pulse (2s in, 2s out)
    lure.pulse(fade_in_time=2, fade_out_time=2)

    # Stomach: slower deep breathing (4s in, 4s out) - out of sync with lure
    stomach.pulse(fade_in_time=4, fade_out_time=4)

    try:
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        lure.close()
        stomach.close()


if __name__ == "__main__":
    main()
