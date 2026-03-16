# pilight

A single pulsing LED driven by a Raspberry Pi Zero 2 W — the glowing "lure" for a wearable Anglerfish prop.

## Wiring

```
GPIO 18 (Pin 12) ---[ 220Ω ]--- LED+ (long leg)
GND    (Pin  6) --------------- LED- (short leg)
```

## Setup on the Pi

```bash
# Clone onto the Pi
git clone https://github.com/YOUR_USER/pilight.git
cd pilight

# Install and enable the auto-start service
sudo bash setup.sh
```

That's it. The LED pulses on boot, survives crashes (auto-restart), and needs no screen or keyboard.

## Manual run

```bash
python3 lure.py
# Ctrl+C to stop
```

## How it works

`gpiozero.PWMLED.pulse()` handles the PWM fade in a background thread. The script just starts the pulse and waits forever. The systemd service ensures it runs on boot and restarts if anything goes wrong.
