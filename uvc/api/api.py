# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from . import log, ENV, PLONE, GROK, UVCLIGHT
from .interface import UVCAPI

from zope.interface.declarations import moduleProvides
from grokcore.component import (
    baseclass, context, name, description,
    order, title, implements, provides, subscribe,
    GlobalUtility)


if ENV is GROK:
    from grokcore.security import require
    from grokcore.chameleon.components import ChameleonPageTemplateFile
    from grokcore.viewlet import viewletmanager, view
    from grokcore.view import View
    from grokcore.layout import Layout, Page
    from megrok.z3ctable import TablePage
    from uvc.layout import Menu, MenuItem, SubMenu
    from uvc.layout.forms import Form
    from zope.security.interfaces import IPrincipal
    from zeam.form.base import Fields, action, Action, SUCCESS

    def get_principal(context, request):
        return request.principal

    def get_template(dir, filename):
        return ChameleonPageTemplateFile(filename, dir)


elif ENV is PLONE:
    from grokcore.security import require
    from grokcore.viewlet import viewletmanager, view
    from uvc.plone.api import Layout, Form, View, Page, Viewlet, Fields, action
    from uvc.plone.api import Action, SUCCESS, FAILURE, ComposedForm, SubForm
    from uvc.plone.api import get_principal, IPrincipal, Actions
    from five.grok import templatedir
    Menu = MenuItem = SubMenu = TablePage = None


elif ENV is UVCLIGHT:
    try:
        from ul.auth import require
    except ImportError:
        pass
    from uvclight.directives import view, viewletmanager
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
