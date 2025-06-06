# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_base import AccountBase
from plaid_skel.models.investment_transaction import InvestmentTransaction
from plaid_skel.models.item import Item
from plaid_skel.models.security import Security




class InvestmentsTransactionsGetResponse(BaseModel):
    """InvestmentsTransactionsGetResponse defines the response schema for `/investments/transactions/get`"""


    item: Item = Field()
    accounts: List[AccountBase] = Field( description="The accounts for which transaction history is being fetched.")
    securities: List[Security] = Field( description="All securities for which there is a corresponding transaction being fetched.")
    investment_transactions: List[InvestmentTransaction] = Field( description="The transactions being fetched")
    total_investment_transactions: int = Field( description="The total number of transactions available within the date range specified. If `total_investment_transactions` is larger than the size of the `transactions` array, more transactions are available and can be fetched via manipulating the `offset` parameter.")
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

InvestmentsTransactionsGetResponse.update_forward_refs()
