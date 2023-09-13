# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class PaystubPayFrequency(str, Enum):
    MONTHLY = "MONTHLY"
    BI_WEEKLY = "BI-WEEKLY"
    WEEKLY = "WEEKLY"
    SEMI_MONTHLY = "SEMI-MONTHLY"

# Nullable OpenAPI enum
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema: dict) -> None:
        field_schema["nullable"] = True
