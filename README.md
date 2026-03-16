# pilight

A single pulsing LED driven by a Raspberry Pi Zero 2 W — the glowing "lure" for a wearable Anglerfish prop.

The prop is a hollowed-out plastic watering can worn over a suit, with a thick wire extending from the top holding a white LED that slowly pulses like a bioluminescent deep-sea lure.

## Hardware

- Raspberry Pi Zero 2 W (headless, Raspberry Pi OS Lite 64-bit)
- 1x 5mm white LED
- 1x 220 ohm resistor
- USB power bank
- Wire for the lure stalk

## Wiring

```
Pi Zero 2 W
┌──────────┐
│      Pin 12 (GPIO 18) ──[ 220Ω ]──── LED+ (long leg)
│      Pin  6 (GND)     ─────────────── LED- (short leg)
└──────────┘
```

## Setup

SSH into the Pi and run:

```bash
sudo apt update && sudo apt install -y git
git clone https://github.com/GerardW-B/pilight.git
cd pilight
sudo bash setup.sh
```

That's it. The LED pulses on boot, survives crashes (auto-restart), and needs no screen or keyboard. Just plug in the power bank and go.

## Manual run

```bash
python3 lure.py
# Ctrl+C to stop
```

## Service commands

```bash
sudo systemctl status lure     # check status
sudo systemctl stop lure       # stop the pulse
sudo systemctl restart lure    # restart
sudo systemctl disable lure    # disable auto-start
```

## How it works

`lure.py` uses `gpiozero.PWMLED.pulse()` to smoothly fade the LED in and out (2 seconds each way) in a continuous loop. `setup.sh` installs a systemd service that starts the script on boot and restarts it automatically if anything goes wrong.
