# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class ActivityType(str, Enum):
    UNKNOWN = "UNKNOWN"
    ITEM_CREATE = "ITEM_CREATE"
    ITEM_IMPORT = "ITEM_IMPORT"
    ITEM_UPDATE = "ITEM_UPDATE"
    ITEM_UNLINK = "ITEM_UNLINK"
    PORTAL_UNLINK = "PORTAL_UNLINK"
    PORTAL_ITEMS_DELETE = "PORTAL_ITEMS_DELETE"
    ITEM_REMOVE = "ITEM_REMOVE"
    INVARIANT_CHECKER_DELETION = "INVARIANT_CHECKER_DELETION"
    SCOPES_UPDATE = "SCOPES_UPDATE"
