# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.

from enum import Enum

from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue


class AssetType(str, Enum):
    CHECKINGACCOUNT = "CheckingAccount"
    SAVINGSACCOUNT = "SavingsAccount"
    INVESTMENT = "Investment"
    MONEYMARKETFUND = "MoneyMarketFund"
    OTHER = "Other"
