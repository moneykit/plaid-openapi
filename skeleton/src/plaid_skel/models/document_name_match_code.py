# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


class DocumentNameMatchCode(str, Enum):
    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NO_MATCH = "no_match"
