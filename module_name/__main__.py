#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Project Name
# Francisco Ribeiro <francisco@ironik.org>
####################################################################################################
#!/usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################################################
"""Project Name.
Usage:
  wire.py
  wire.py ship new <name>...
  wire.py ship <name> move <x> <y> [--speed=<kn>]
  wire.py ship shoot <x> <y>
  wire.py mine (set|remove) <x> <y> [--moored|--drifting]
  wire.py -S | --shell
  wire.py -D | --debug
  wire.py -h | --help
  wire.py -v | --verbose
  wire.py --version

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
import os, logging
from .change_me import main

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

if __name__.endswith('__main__'):
    logger.info("%s started" % settings.PROG_NAME)

    if arguments['--shell']:
        from .model import *
        try:
            import IPython
            IPython.embed()
        except ImportError:
            import code
            code.interact(local=locals())
    elif arguments['--debug']:
        import pdb
        pdb.set_trace()

    main()
