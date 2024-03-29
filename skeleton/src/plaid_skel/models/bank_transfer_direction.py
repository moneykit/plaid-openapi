# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class BankTransferDirection(str, Enum):
    OUTBOUND = "outbound"
    INBOUND = "inbound"

# Nullable OpenAPI enum
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: dict) -> None:
        field_schema["nullable"] = True
