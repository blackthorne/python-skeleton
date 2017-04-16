#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Project Name
####################################################################################################
"""Project Name.
Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored|--drifting]
  naval_fate.py -h | --help
  naval_fate.py --version
  
Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
"""
####################################################################################################
# program initialisation

__author__ = 'Francisco Ribeiro <francisco@ironik.org>'
__version__ = '0.1'

from docopt import docopt
from model import LockedClass # rename accordingly
import sys, os, logging, settings


# logging
logger = logging.getLogger(settings.PROG_NAME)

# create a file handler
handler = logging.FileHandler(os.path.join(settings.logs_folder, '%s.log' % settings.PROG_NAME))
console_handler = logging.StreamHandler()

if(settings.LOGGING_VERBOSITY == 'DEBUG'):
    logger.setLevel(logging.DEBUG)
    handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)

# create a logging format                                                                                                                       
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# add the handlers to the logger                                                                                                                
logger.addHandler(handler)
logger.addHandler(console_handler)

logger.info("%s started" % settings.PROG_NAME)

####################################################################################################
# Program Logic

def main():
    """Main entry point for the script"""
    pass

if __name__ == '__main__':
    arguments = docopt(__doc__, version="%s v%s" % (settings.PROG_NAME.capitalize(), __version__))
    sys.exit(main())