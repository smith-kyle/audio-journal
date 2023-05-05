#!/bin/bash

# Check if the script is being run as root (using sudo)
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run with sudo."
    exit 1
fi

# Run the Python script with warnings suppressed
PYTHONWARNINGS="ignore" python ./main.py