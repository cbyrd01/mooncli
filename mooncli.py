#!/usr/bin/env python3
"""
MoonrakerCLI

Command Line Interface for Moonraker and Klipper to control a 3D printer

Author: Christopher Byrd
Date: 02/06/2023
"""

import fire
import moonrakerpy as moonpy


class MoonCLI(object):

    def __init__(self, method="http", ip="127.0.0.1"):
        # Instantiate a `MoonrakerPrinter` object using the web/IP address of the target
        # Moonraker installation.
        self._method = method
        self._url = self._method + "://" + ip + "/"
        self._printer = moonpy.MoonrakerPrinter(self._url)

    def gcode(self, *gcode):
        code = ' '.join(gcode)
        print(f"Sending G-code command: {code} to {self._url}...")
        self._printer.send_gcode(code)

    def settemp(self, heater, temp):
        print(f"setting {heater} to {temp}")
        # if heater == 'extruder':
        # printer.set_extruder_temp(0)
        # elif heater == 'bed':
        # printer.set_bed_temp(0)

    def gettemp(self, heater):
        print(f"Getting {heater} temp")
        # if heater == 'extruder':
        # printer.query_temperatures()
        # elif heater == 'bed':
        # printer.query_temperatures()


if __name__ == "__main__":

    fire.Fire(MoonCLI)
