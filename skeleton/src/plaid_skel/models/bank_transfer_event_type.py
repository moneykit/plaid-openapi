# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class BankTransferEventType(str, Enum):
    PENDING = "pending"
    CANCELLED = "cancelled"
    FAILED = "failed"
    POSTED = "posted"
    REVERSED = "reversed"
