# Python Skeleton Project
This is a starting point for python projects that I use. Whilst opinionated, this is a simple code structure that can be used to bootstrap many different Python projects.

Written for Python 2 but should work with 3

Requirements: **hypothesis, docopt** (optional)

Status: **stable**

### Features:
* suitable for both Python v2 and v3
* initializes logging for both terminal and file logs
* simplistic DEBUG mode to tune logging verbosity
* includes bootstrap code for 2 different types of tests: unittests and property based (hypothesis)
* test files can be invoked alltogether (nose, py.test) but can also be invoked separately
* configuration settings on separate file (settings.py)
* models with customised classes on separate file (model.py)
* command line argument parsing from help message in docstring (docopt)
* LICENSE file included (Apache v2.0)
* packaging files (requirements.txt, setup.py, __init__.py)
* Makefile (init, test, clean)
* main logic separate from program initilization (__main__.py)
* separate locations for both program data and logs
* does not rely on IDE customisations to work
* .gitignore file

### Things that I do not like about it:
* ~~Logging - it would be nice to somehow move logging initialisation code somewhere else outside of the main script so it could go straight into the main logic~~ - done, __main__.py is now used to initialize project, main logic goes to <module_name>.py
* Test PATH manipulation - whilst I want tests to be on a separate folder and outside of the package itself, they need access to the functions to be tested which means that each file needs to have python's PATH updated. An alternative would be to add it manually on your IDE
* ~~having to update version twice for each release (in main script and in setup.py)~~ - done, use _make_

### Instructions:
1. start your project by filling setup.py
1. run _make_ from within the project folder (you can update your program at anytime by running it again)
1. update docstring within the module_name/__main__.py file
1. review requirements.txt in the main project folder and the remaining files within the module folder
1. rename module_name.py file to your preferred program name and kick off!
1. before your first commit, review README.me (this file) and updated your tests/

### _Make_ targets:
* setup (default) - updates author, version and project_name settings in your project
* dist - builds a tar.gz (in dist/) with code and other files relevant for distribution such as LICENSE and README files
* deps - installs dependencies (according to requirements.txt)
* tests - runs tests
* clean - deletes .pyc files as well as all logs and tests metadata
* install - installs package
* also refer to setup.py for more options

### Installation:
You can install this project _as is_ with:

```
$ pip install . --user
```