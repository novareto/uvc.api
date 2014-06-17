# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute


class UVCBrowserComponents(Interface):

    Layout = Attribute(
        "Layout component to render consistent HTML.")
    
    Form = Attribute(
        "Form component.")

    View = Attribute(
        "Standalone browser component.")

    Page = Attribute(
        "View rendered inside a Layout component.")

    TablePage = Attribute(
        "Table rendered inside a Layout component.")

    Menu = Attribute(
        "Menu component managing menu items.")

    SubMenu = Attribute(
        "Menu component subordoned to an other menu component.")

    MenuItem = Attribute(
        "Menu items component, subordoned to a menu or submenu.")


class UVCSecurity(Interface):

    IPrincipal = Attribute(
        "Interface representing an interaction actor.")

    get_principal = Attribute(
        "Method that returns the current active IPrincipal component.")


class UVCAPI(UVCBrowserComponents, UVCSecurity):
    pass
