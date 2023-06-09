# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum


class DepositoryAccountSubtype(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    HSA = "hsa"
    CD = "cd"
    MONEY_MARKET = "money market"
    PAYPAL = "paypal"
    PREPAID = "prepaid"
    CASH_MANAGEMENT = "cash management"
    EBT = "ebt"
    ALL = "all"
