#!/usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################################################
"""Project Name.
Usage:
  naval_fate.py
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -S | --shell
  naval_fate.py -D | --debug
  naval_fate.py -h | --help
  naval_fate.py -v | --verbose
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  -v --verbose  Verbose mode.
  -S --shell    Loads (i)Python shell within the app context.
  -D --debug    Loads app with debugger at entry point.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""
####################################################################################################
# program initialisation

#__all__ = ['submodule1', 'submodule2']
__author__ = 'Francisco Ribeiro <francisco@ironik.org>'
__version__ = '0.1'

from docopt import docopt
from . import settings
import sys, os, logging

# errors
UNKNOWN_ERROR = -1

# logging
logger = logging.getLogger(settings.PROG_NAME)
if not logger.handlers:

    # create a file handler
    handler = logging.FileHandler(os.path.join(settings.logs_folder, '%s.log' % settings.PROG_NAME))
    console_handler = logging.StreamHandler()

    # setting right level of logging verbosity
    logger.setLevel(settings.LOGGING_VERBOSITY)
    handler.setLevel(settings.LOGGING_VERBOSITY)
    console_handler.setLevel(settings.LOGGING_VERBOSITY)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(console_handler)

arguments = docopt(__doc__, version="%s v%s" % (settings.PROG_NAME.capitalize(), __version__))
