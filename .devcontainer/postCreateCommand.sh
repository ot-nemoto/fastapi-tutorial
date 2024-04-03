#!/bin/sh
# postCreateCommand.sh

sudo apt update

sudo ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

pip install -r requirements.txt