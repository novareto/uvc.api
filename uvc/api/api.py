# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

from os import path
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
    from grokcore.layout import Page as BasePage
    from megrok.z3ctable import TablePage
    from uvc.layout import Menu, MenuItem, SubMenu
    from uvc.layout.forms import Form
    from zope.security.interfaces import IPrincipal
    from zope.session.interfaces import ISession
    from zeam.form.base import Fields, action, Action, SUCCESS
    from grok.components import ViewSupportMixin

    def get_principal(context, request):
        return request.principal

    def get_template(filename, dir):
        dir = path.join(path.dirname(dir), 'templates')
        return ChameleonPageTemplateFile(filename, dir)

    class Page(ViewSupportMixin, BasePage):
        baseclass()

    class TablePage(ViewSupportMixin, TablePage):
        baseclass()



elif ENV is PLONE:
    from grokcore.security import require
    from grokcore.viewlet import viewletmanager, view
    from zope.session.interfaces import ISession
    from uvc.plone.api import Layout, Form, View, Page, Viewlet, Fields, action
    from uvc.plone.api import Action, SUCCESS, FAILURE, ComposedForm, SubForm
    from uvc.plone.api import get_principal, IPrincipal, Actions
    from uvc.plone.api import ViewletManager
    from five.grok import templatedir
    Menu = MenuItem = SubMenu = TablePage = None


elif ENV is UVCLIGHT:
    try:
        from ul.auth import require
    except ImportError:
        pass
    from uvclight.directives import view, viewletmanager
    from uvclight import menu, get_template
    from uvclight import Layout, Viewlet, Page, View
    from uvclight import action, Fields, Form, DisplayForm, AddForm, EditForm
    from uvclight import Menu, MenuItem, SubMenu, TablePage
    from uvclight.utils import current_principal as get_principal
    from cromlech.browser.interfaces import ISession
    from zope.security.interfaces import IPrincipal
    from cromlech.browser import slot as viewletmanager

else:
    raise NotImplementedError


moduleProvides(UVCAPI)
__all__ = list(UVCAPI)
