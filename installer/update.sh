#!/bin/bash

echo "Updating Monarch..."

cd /opt/Monarch || exit

git pull

echo "⚔ Update completed."