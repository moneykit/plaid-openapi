# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


class WeakAliasDetermination(str, Enum):
    NONE = "none"
    SOURCE = "source"
    PLAID = "plaid"
