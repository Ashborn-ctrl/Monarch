#!/bin/bash

echo "Updating Monarch..."

cd /opt/Monarch || exit

git pull origin main

echo "⚔ Update completed."