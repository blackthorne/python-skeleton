#!/usr/bin/env python
# coding: utf-8
#
# Settings
####################################################################################################
import os, logging

# folder locations
project_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
dataset_folder = os.path.abspath(os.path.join(project_folder, 'data'))
logs_folder = os.path.abspath(os.path.join(project_folder, 'logs'))

LOGGING_VERBOSITY = logging.DEBUG
PROG_NAME = os.path.basename(os.path.dirname(project_folder))

