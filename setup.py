# -*- coding: utf-8 -*-
import distutils.cmd
import distutils.log
import setuptools
import subprocess

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='module_name',
    version='0.1',
    description='yada yada yada',
    long_description=readme,
    author='Francisco Ribeiro',
    author_email='francisco@ironik.org',
    url='https://github.com/blackthorne/libcall',
    license=license,
    packages=setuptools.find_packages(exclude=('tests', 'docs', 'logs', 'dist'))
)




# (setup, deps, tests, clean, cleanall, install, dist)

#@TODO: to add custom commands and replace Makefile
# class PylintCommand(distutils.cmd.Command):
#   """A custom command to run Pylint on all Python source files."""
#
#   description = 'run Pylint on Python source files'
#   user_options = [
#       # The format is (long option, short option, description).
#       ('pylint-rcfile=', None, 'path to Pylint config file'),
#   ]
#
#   def initialize_options(self):
#     """Set default values for options."""
#     # Each user option must be listed here with their default value.
#     self.pylint_rcfile = ''
#
#   def finalize_options(self):
#     """Post-process options."""
#     if self.pylint_rcfile:
#       assert os.path.exists(self.pylint_rcfile), (
#           'Pylint config file %s does not exist.' % self.pylint_rcfile)
#
#   def run(self):
#     """Run command."""
#     command = ['/usr/bin/pylint']
#     if self.pylint_rcfile:
#       command.append('--rcfile=%s' % self.pylint_rcfile)
#     command.append(os.getcwd())
#     self.announce(
#         'Running command: %s' % str(command),
#         level=distutils.log.INFO)
#     subprocess.check_call(command)
#
#
# setuptools.setup(
#     cmdclass={
#         'pylint': PylintCommand,
#     },
#     # Usual setup() args.
#     # ...
# )
