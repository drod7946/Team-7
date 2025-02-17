#!/bin/bash
set -u -e
xfce4-terminal --command="python3 udpserver.py"
python3 udpclient.py