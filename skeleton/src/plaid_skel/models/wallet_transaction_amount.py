# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import field_validator, AnyUrl, BaseModel, EmailStr, Field  # noqa: F401
from plaid_skel.models.wallet_iso_currency_code import WalletISOCurrencyCode




class WalletTransactionAmount(BaseModel):
    """The amount and currency of a transaction"""


    iso_currency_code: WalletISOCurrencyCode = Field()
    value: float = Field( description="The amount of the transaction. Must contain at most two digits of precision e.g. `1.23`.")

    @field_validator("value")
    @classmethod
    def value_min(cls, value):
        assert value >= 0.01
        return value

WalletTransactionAmount.update_forward_refs()
