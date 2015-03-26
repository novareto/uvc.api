# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from zope.interface.declarations import moduleProvides
from grokcore.viewlet import viewletmanager, view
from grokcore.component import baseclass, context, name, description
from grokcore.component import order, title, implements, provides, subscribe
from grokcore.component import GlobalUtility
from grokcore.security import require

from . import log, ENV, PLONE, GROK, UVCLIGHT
from .interface import UVCAPI


if ENV is GROK:
    from grokcore.view import View
    from grokcore.layout import Layout, Page
    from megrok.z3ctable import TablePage
    from uvc.layout import Menu, MenuItem, SubMenu
    from uvc.layout.forms import Form
    from zope.security.interfaces import IPrincipal
    from zeam.form.base import Fields, action, Action, SUCCESS

    def get_principal(context, request):
        return request.principal


elif ENV is PLONE:
    from uvc.plone.api import Layout, Form, View, Page, Viewlet, Fields, action
    from uvc.plone.api import Action, SUCCESS, FAILURE, ComposedForm, SubForm
    from uvc.plone.api import get_principal, IPrincipal, Actions
    from five.grok import templatedir
    Menu = MenuItem = SubMenu = TablePage = None


elif ENV is UVCLIGHT:
    from uvclight import Viewlet, Fields, action, DisplayForm, AddForm, EditForm, Layout, Form, Page, View
    from uvclight.utils import current_principal as get_principal
    from zope.security.interfaces import IPrincipal
    from uvclight import Menu, MenuItem, SubMenu, TablePage
    from uvclight import menu
    from cromlech.browser import slot as viewletmanager

else:
    raise NotImplementedError


moduleProvides(UVCAPI)
__all__ = list(UVCAPI)
