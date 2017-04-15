#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from module_name.a import is_valid_login
import logging
import unittest

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',)

logger = logging.getLogger(__name__)
logger.debug('tests beginning..')

class UnitTest(unittest.TestCase):

    # describe WHATEVER
    def test_WHATEVER(self):
        self.assertFalse(is_valid_login('user','pass'))

if __name__ == '__main__':
    unittest.main()
    logger.info('END OF TESTS')

# test.setUp = setup_test
# test.tearDown = cleanup_after_test