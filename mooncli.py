#!/usr/bin/env python3
"""
MoonrakerCLI

Command Line Interface for Moonraker and Klipper to control a 3D printer

Author: Christopher Byrd
Date: 02/06/2023
"""

import fire
import moonrakerpy as moonpy


def gcode(command):
    print(f"Sending G-code command: {command}...")
    # printer.send_gcode(command)


def settemp(heater, temp):
    print(f"setting {heater} to {temp}")
    # if heater == 'extruder':
    # printer.set_extruder_temp(0)
    # elif heater == 'bed':
    # printer.set_bed_temp(0)


def gettemp(heater):
    print(f"Getting {heater} temp")
    # if heater == 'extruder':
    # printer.query_temperatures()
    # elif heater == 'bed':
    # printer.query_temperatures()


if __name__ == "__main__":
    # Instantiate a `MoonrakerPrinter` object using the web/IP address of the target
    # Moonraker installation.
    printer = moonpy.MoonrakerPrinter("http://192.168.1.54/")
    fire.Fire()
