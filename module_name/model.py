#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect, settings, logging

logger = logging.getLogger(settings.PROG_NAME)

class Finding:
    """
    represents a potential finding
    """

    def __init__(self):
        """define a finding"""
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        logger.debug("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        logger.debug("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        logger.debug("deleter of x called")
        del(self._x)

    def __str__(self):
        pass


class LockedClass(object):
    """
    implements locked class where gets and sets are only reachable through public methods and provides auditability
    """

    __slots__ = ['balance', 'account_type']

    def __init__(self, initial_balance=0, account_type='basic'):
        self.balance = initial_balance
        self.account_type = account_type

    def __setattr__(self, name, val):
        super(LockedClass, self).__setattr__(name, val)
        logger.debug("[!]", name, "set to", val)

    def __getattribute__(self, name):
        logger.debug("[!]", name, "called from", \
            inspect.getouterframes(inspect.currentframe())[1][1:4])

        # use proper logging facility
        return super(LockedClass, self).__getattribute__(name)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __reset(self):
        self.balance = 0