# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class WalletTransactionStatus(str, Enum):
    AUTHORISING = "AUTHORISING"
    INITIATED = "INITIATED"
    EXECUTED = "EXECUTED"
    SETTLED = "SETTLED"
    BLOCKED = "BLOCKED"
    FAILED = "FAILED"
