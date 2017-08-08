#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Project Name
# Francisco Ribeiro <francisco@ironik.org>
####################################################################################################

from . import settings
from .__init__ import logger, arguments

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
