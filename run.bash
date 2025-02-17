#!/bin/bash
set -u -e
xfce4-terminal -- python3 udpserver.py
python3 udpclient.py