# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.account_base import AccountBase
from plaid_skel.models.holding import Holding
from plaid_skel.models.item import Item
from plaid_skel.models.security import Security




class InvestmentsHoldingsGetResponse(BaseModel):
    """InvestmentsHoldingsGetResponse defines the response schema for `/investments/holdings/get`"""


    accounts: List[AccountBase] = Field( description="The accounts associated with the Item")
    holdings: List[Holding] = Field( description="The holdings belonging to investment accounts associated with the Item. Details of the securities in the holdings are provided in the `securities` field. ")
    securities: List[Security] = Field( description="Objects describing the securities held in the accounts associated with the Item. ")
    item: Item = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

InvestmentsHoldingsGetResponse.update_forward_refs()
