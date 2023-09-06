#!/usr/bin/env python
# coding: utf-8
#
# Settings
####################################################################################################
import os, logging
from .binds import *

# folder locations
project_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
data_folder = os.path.abspath(os.path.join(project_folder, 'data'))
logs_folder = os.path.abspath(os.path.join(project_folder, 'logs'))
static_folder = os.path.abspath(os.path.join(project_folder, 'static'))

LOGGING_VERBOSITY = logging.DEBUG
PROG_NAME = 'change_me'