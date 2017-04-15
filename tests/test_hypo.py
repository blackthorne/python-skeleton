#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from module_name.a import is_valid_login

import hypothesis.strategies as st
from hypothesis import given, assume, settings, Verbosity

#@settings(verbosity=Verbosity.verbose)
@given(st.text(), st.text())
def test_is_valid_login(username, password):
    assert is_valid_login(username, password) is False
