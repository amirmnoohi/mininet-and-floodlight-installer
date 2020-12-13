#!/usr/bin/env bash
git clone https://git.noohi.org/amirmnoohi/mininet-and-floodlight
# shellcheck disable=SC2035
cd "mininet-and-floodlight" && mv * .. && cd .. && apt install python -y && clear && sudo python install.py