# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from uvc.api import log
from uvc.api import ENV, PLONE, GROK, UVCLIGHT
from zope import interface
from zope.interface.declarations import moduleProvides
from .interface import UVCAPI
from grokcore.component import baseclass, context, name
from grokcore.component import order, title, implements, provides
from grokcore.security import require


if ENV is GROK:
    from uvcsite import Form, Page, View
    from zope.security.interfaces import IPrincipal

    def get_principal(context, request):
        return request.principal

elif ENV is PLONE:
    from uvc.plone.api import Layout, Form, View, Page
    from uvc.plone.api import get_principal, IPrincipal
    from five.grok import templatedir

elif ENV is UVCLIGHT:
    from uvclight import Layout, Form, Page, View
    from uvclight.utils import current_principal as get_principal
    from zope.security.interfaces import IPrincipal

else:
    raise NotImplementedError


moduleProvides(UVCAPI)
__all__ = list(UVCAPI)
