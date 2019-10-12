# Light-Control-RPi
A small script to control Xiaomi Yeelights from a GUI in Python.

This script uses the following libraries:
- ~~guizero: A quick and simple Python library to create basic GUIs~~
- kivy: A python library to create GUIs
- yeelight: A library to control Xiaomi Yeelights.

## What to do first
Before this script can work, you have to replace lights IPs on it.
Then go on the Yeelight app on your phone, and turn on the LAN controls for each Bulb.
Install guizero and yeelight using pip3

## Working functionalities
- Switch between different rooms
- Toggle lights of each room (On / Off)
- Change luminosity (Due to the Yeelight restrictions, you may be limited in number of luminosity changes per minute)
