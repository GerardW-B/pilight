#!/usr/bin/env bash
# Run this on the Pi to install the systemd service.
# Usage: sudo bash setup.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SERVICE_FILE="/etc/systemd/system/lure.service"

cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=Anglerfish LEDs (lure + stomach)
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 ${SCRIPT_DIR}/lure.py
WorkingDirectory=${SCRIPT_DIR}
Restart=always
RestartSec=3
User=root

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable lure.service
systemctl start lure.service

echo "Done. Both LEDs should be pulsing now."
echo "It will start automatically on every boot."
echo ""
echo "Useful commands:"
echo "  sudo systemctl status lure    # check status"
echo "  sudo systemctl stop lure      # stop"
echo "  sudo systemctl restart lure   # restart"
