# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class TransferEventListTransferType(str, Enum):
    DEBIT = "debit"
    CREDIT = "credit"

# Nullable OpenAPI enum
    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema["nullable"] = True
