#!/usr/bin/python3
"""The robot module, provides an python interface to the RoboCon hardware and
April tags a marker recognition system. Also performs convience functions to
allow logging to sheep our in-browser editor"""
import sys

MINIUM_VERSION = (3, 7)
try:
    assert sys.version_info >= MINIUM_VERSION
except:
    raise ImportError("Expected at least python {} but instead got {}".format(
            MINIUM_VERSION, sys.version_info))

# This log import configures our logging for us, but we don't want to
# provide it as part of this package.
from robot import log as _log

from robot.wrapper import Robot, NoCameraPresent
from robot.greengiant import OUTPUT, INPUT, INPUT_ANALOG, INPUT_PULLUP
from robot.vision import MARKER_ARENA, MARKER_TOKEN


__all__ = ["Robot", "NoCameraPresent", "OUTPUT", "INPUT", "INPUT_ANALOG",
           "INPUT_PULLUP", "MARKER_ARENA", "MARKER_TOKEN"]
