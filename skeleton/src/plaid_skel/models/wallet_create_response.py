# coding: utf-8
# AUTOGENERATED with MDM customization.  Do not edit.




from __future__ import annotations
from datetime import date as date_  # noqa: F401
from datetime import datetime as datetime_  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from plaid_skel.models.wallet_balance import WalletBalance
from plaid_skel.models.wallet_numbers import WalletNumbers
from plaid_skel.models.wallet_status import WalletStatus




class WalletCreateResponse(BaseModel):
    """WalletCreateResponse defines the response schema for `/wallet/create`"""


    wallet_id: str = Field( description="A unique ID identifying the e-wallet")
    balance: WalletBalance = Field()
    numbers: WalletNumbers = Field()
    recipient_id: Optional[str] = Field(default=None, description="The ID of the recipient that corresponds to the e-wallet account numbers")
    status: WalletStatus = Field()
    request_id: str = Field( description="A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.")

WalletCreateResponse.update_forward_refs()
