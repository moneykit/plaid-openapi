# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class SignalPaymentMethod(str, Enum):
    SAME_DAY_ACH = "SAME_DAY_ACH"
    NEXT_DAY_ACH = "NEXT_DAY_ACH"
    STANDARD_ACH = "STANDARD_ACH"
    REAL_TIME_PAYMENTS = "REAL_TIME_PAYMENTS"
    DEBIT_CARD = "DEBIT_CARD"
    MULTIPLE_PAYMENT_METHODS = "MULTIPLE_PAYMENT_METHODS"

# Nullable OpenAPI enum
    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema["nullable"] = True
