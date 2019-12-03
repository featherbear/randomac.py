#!/usr/bin/python3

from os import system as exec
import sys

RADIO_ON = "nmcli radio wifi on"
RADIO_OFF = "nmcli radio wifi off"
RESET_MAC = "macchanger -p wlan0"
RANDOMISE_MAC = "macchanger -r -b wlan0"

def resetMAC(*args, **kwargs):
  if len(args) != 0:
    print("No arguments required, ignoring arguments")
  exec(RADIO_OFF)
  exec(RESET_MAC)
  exec(RADIO_ON)

def randomiseMAC(*args, **kwargs):
  if len(args) != 0:
    print("No arguments required, ignoring arguments")
  exec(RADIO_OFF)
  exec(RANDOMISE_MAC)
  exec(RADIO_ON)


commands = {
  "reset": resetMAC,
  "random": randomiseMAC
}

if __name__ == "__main__":
  if len(sys.argv) == 1 or sys.argv[1] not in commands:
    print(f"{sys.argv[0]} " + "|".join(commands.keys()))
    sys.exit()

  command = sys.argv[1]
  if command in commands:
    commands[command](*sys.argv[2:])
