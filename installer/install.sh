#!/bin/bash

echo "⚔ Installing Monarch Toolkit..."

INSTALL_DIR="/opt/Monarch"
BIN_PATH="/usr/bin/Arise"

if [ -d "$INSTALL_DIR" ]; then
    echo "Monarch already installed."
    exit 1
fi

echo "Cloning repository..."

sudo git clone https://github.com/Ashborn-ctrl/Monarch.git $INSTALL_DIR

echo "Creating launcher..."

echo '#!/bin/bash
python3 /opt/Monarch/core/main.py' | sudo tee $BIN_PATH > /dev/null

sudo chmod +x $BIN_PATH

echo "👑 Monarch installed successfully!"
echo "Run using command: Arise"