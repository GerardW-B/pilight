#!/usr/bin/env python3
"""
Anglerfish Lure - A single pulsing LED for a wearable prop.

Hardware:
    LED+ -> 220ohm resistor -> GPIO 18 (Pin 12)
    LED- -> GND (Pin 6)
"""

from gpiozero import PWMLED
from signal import pause
import sys


def main():
    led = PWMLED(18)

    # Slow bioluminescent pulse: 2s fade in, 2s fade out
    led.pulse(fade_in_time=2, fade_out_time=2)

    try:
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        led.close()


if __name__ == "__main__":
    main()
