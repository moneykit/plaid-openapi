# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class PaymentScheme(str, Enum):
    LOCAL_DEFAULT = "LOCAL_DEFAULT"
    LOCAL_INSTANT = "LOCAL_INSTANT"
    SEPA_CREDIT_TRANSFER = "SEPA_CREDIT_TRANSFER"
    SEPA_CREDIT_TRANSFER_INSTANT = "SEPA_CREDIT_TRANSFER_INSTANT"

# Nullable OpenAPI enum
    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema["nullable"] = True
