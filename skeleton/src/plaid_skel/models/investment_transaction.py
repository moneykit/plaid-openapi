# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.investment_transaction_subtype import InvestmentTransactionSubtype
from plaid_skel.models.investment_transaction_type import InvestmentTransactionType




class InvestmentTransaction(BaseModel):
    """A transaction within an investment account."""


    investment_transaction_id: str = Field( description="The ID of the Investment transaction, unique across all Plaid transactions. Like all Plaid identifiers, the `investment_transaction_id` is case sensitive.")
    cancel_transaction_id: Optional[str] = Field(default=None, description="A legacy field formerly used internally by Plaid to identify certain canceled transactions.")
    account_id: str = Field( description="The `account_id` of the account against which this transaction posted.")
    security_id: Optional[str] = Field(default=None, description="The `security_id` to which this transaction is related.")
    date: date_ = Field( description="The [ISO 8601](https://wikipedia.org/wiki/ISO_8601) posting date for the transaction.")
    name: str = Field( description="The institution’s description of the transaction.")
    quantity: float = Field( description="The number of units of the security involved in this transaction. Positive for buy transactions; negative for sell transactions.")
    amount: float = Field( description="The complete value of the transaction. Positive values when cash is debited, e.g. purchases of stock; negative values when cash is credited, e.g. sales of stock. Treatment remains the same for cash-only movements unassociated with securities.")
    price: float = Field( description="The price of the security at which this transaction occurred.")
    fees: Optional[float] = Field(default=None, description="The combined value of all fees applied to this transaction")
    type: InvestmentTransactionType = Field()
    subtype: InvestmentTransactionSubtype = Field()
    iso_currency_code: Optional[str] = Field(default=None, description="The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-`null`.")
    unofficial_currency_code: Optional[str] = Field(default=None, description="The unofficial currency code associated with the holding. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](https://plaid.com/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.")

InvestmentTransaction.update_forward_refs()
