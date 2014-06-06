# -*- coding: utf-8 -*-

import logging
from grokcore.component import zcml
from zope.interface.verify import verifyObject
from .interface import UVCAPI

logger = logging.getLogger('uvc.api')


def log(message, summary='', severity=logging.INFO):
    logger.log(severity, '%s %s', summary, message)


def skip_tests_path(name):
    return name in ['tests', 'ftests', 'testing',
                    'uvcsite_registrations', 'plone_registrations']

zcml.skip_tests = skip_tests_path


GROK = object()
UVCLIGHT = object()
PLONE = object()


def get_technology():

    try:
        import uvclight
        ENV = UVCLIGHT
        return ENV
    except ImportError:
        pass

    try:
        import grok
        ENV = GROK
        return ENV
    except ImportError:
        pass

    try:
        import five.grok
        ENV = PLONE
        return ENV
    except ImportError:
        raise NotImplementedError(
            'No library available. Make sure you have at least one of '
            'these : Plone, Grok, Cromlech.')


ENV = get_technology()

from . import api
assert verifyObject(UVCAPI, api)
