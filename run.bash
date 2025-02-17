#!/bin/bash
set -u -e
gnome-terminal -- python3 udpserver.py
python3 udpclient.py