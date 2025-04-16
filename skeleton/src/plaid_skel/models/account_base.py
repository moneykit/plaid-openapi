# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_balance import AccountBalance
from plaid_skel.models.account_subtype import AccountSubtype
from plaid_skel.models.account_type import AccountType




class AccountBase(BaseModel):
    """A single account at a financial institution."""


    account_id: str = Field( description="Plaid’s unique identifier for the account. This value will not change unless Plaid can't reconcile the account with the data returned by the financial institution. This may occur, for example, when the name of the account changes. If this happens a new `account_id` will be assigned to the account.  The `account_id` can also change if the `access_token` is deleted and the same credentials that were used to generate that `access_token` are used to generate a new `access_token` on a later date. In that case, the new `account_id` will be different from the old `account_id`.  If an account with a specific `account_id` disappears instead of changing, the account is likely closed. Closed accounts are not returned by the Plaid API.  Like all Plaid identifiers, the `account_id` is case sensitive.")
    balances: AccountBalance = Field()
    mask: Optional[str] = Field(default=None, description="The last 2-4 alphanumeric characters of an account's official account number. Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.")
    name: str = Field( description="The name of the account, either assigned by the user or by the financial institution itself")
    type: AccountType = Field()
    subtype: Optional[AccountSubtype] = Field(default=None,)

AccountBase.update_forward_refs()
