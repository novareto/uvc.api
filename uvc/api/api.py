# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from zope.interface.declarations import moduleProvides
from grokcore.viewlet import viewletmanager, view
from grokcore.component import baseclass, context, name
from grokcore.component import order, title, implements, provides
from grokcore.security import require

from . import log, ENV, PLONE, GROK, UVCLIGHT
from .interface import UVCAPI


if ENV is GROK:
    from uvc.layout import Layout, TablePage, Page, View
    from uvc.layout import Menu, MenuItem, SubMenu
    from uvc.layout.forms import Form
    from zope.security.interfaces import IPrincipal
    
    def get_principal(context, request):
        return request.principal


elif ENV is PLONE:
    from uvc.plone.api import Layout, Form, View, Page, Viewlet, Fields, action
    from uvc.plone.api import get_principal, IPrincipal
    from five.grok import templatedir
    Menu = MenuItem = SubMenu = TablePage = None
    
    
elif ENV is UVCLIGHT:
    from uvclight import Layout, Form, Page, View
    from uvclight.utils import current_principal as get_principal
    from zope.security.interfaces import IPrincipal
    Menu = MenuItem = SubMenu = TablePage = None
    
else:
    raise NotImplementedError


moduleProvides(UVCAPI)
__all__ = list(UVCAPI)
