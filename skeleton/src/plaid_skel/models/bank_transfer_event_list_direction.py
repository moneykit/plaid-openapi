# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


class BankTransferEventListDirection(str, Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    # Nullable OpenAPI enum
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: dict, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        schema = handler(field_schema)
        schema["nullable"] = True
        return schema
